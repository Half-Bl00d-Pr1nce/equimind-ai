from fastapi import HTTPException
from fastapi import APIRouter
from app.services.parser.html_parser import HTMLParser
from app.services.sec.sec_service import SECService
from app.services.parser.cleaner import DocumentCleaner
from app.services.chunking.chunk_service import ChunkService
from app.services.pipeline.document_pipeline import DocumentPipeline

pipeline = DocumentPipeline()

chunker = ChunkService()

cleaner = DocumentCleaner()

router = APIRouter()

parser = HTMLParser()
sec_service = SECService()


@router.get("/parser/{ticker}", tags=["Parser"])
def parse_filing(ticker: str):

    company = sec_service.get_cik(ticker)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker.upper()}' not found."
        )

    download_info = sec_service.download_latest_10k(
        company["cik"]
    )
    if download_info is None:
        raise HTTPException(
            status_code=404,
            detail="No 10-K filing found."
        )
        
    chunks = pipeline.process(
        download_info["file"]
    )

    return {
        "num_chunks": len(chunks),
        "first_chunk": chunks[0],
    }