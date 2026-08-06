from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.services.embeddings.embedding_service import EmbeddingService
from app.services.pipeline.document_pipeline import DocumentPipeline
from app.services.sec.sec_service import SECService
from app.services.vector_db.qdrant_service import QdrantService

router = APIRouter()

pipeline = DocumentPipeline()
sec = SECService()
embedding = EmbeddingService()
qdrant = QdrantService()

EMBEDDING_DIMENSION = 384


@router.get("/vector/test", tags=["Vector DB"])
def test_connection():

    collections = qdrant.client.get_collections()

    return collections


@router.post("/vector/create", tags=["Vector DB"])
def create_collection():

    qdrant.create_collection(
        EMBEDDING_DIMENSION
    )

    return {
        "status": "Collection created successfully."
    }


@router.post("/vector/index/{ticker}", tags=["Vector DB"])
def index_company(ticker: str):

    company = sec.get_cik(ticker)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker.upper()}' not found."
        )

    qdrant.create_collection(
        EMBEDDING_DIMENSION
    )

    existing_vectors = qdrant.company_vector_count(
        ticker
    )

    if existing_vectors > 0:

        return {
            "status": "Company already indexed.",
            "indexed": True,
            "ticker": ticker.upper(),
            "vector_count": existing_vectors,
        }

    download = sec.download_latest_10k(
        company["cik"]
    )

    if download is None:
        raise HTTPException(
            status_code=404,
            detail=f"No 10-K filing found for ticker '{ticker.upper()}'."
        )

    chunks = pipeline.process(
        download["file"]
    )

    if not chunks:
        raise HTTPException(
            status_code=404,
            detail="No chunks generated."
        )

    embeddings = embedding.embed_chunks(
        chunks
    )

    qdrant.upload_chunks(
        ticker,
        chunks,
        embeddings,
    )

    return {
        "status": "Indexed successfully.",
        "indexed": True,
        "ticker": ticker.upper(),
        "chunks": len(chunks),
    }


@router.get("/vector/count", tags=["Vector DB"])
def count_vectors():

    info = qdrant.client.get_collection(
        qdrant.COLLECTION_NAME
    )

    return {
        "vectors": info.points_count
    }


@router.get(
    "/vector/search",
    tags=["Vector DB"],
)
def search(
    ticker: str = Query(...),
    query: str = Query(...),
):

    query_embedding = embedding.embed(query)

    results = qdrant.search(
        ticker,
        query_embedding,
    )

    return {
        "results": results
    }