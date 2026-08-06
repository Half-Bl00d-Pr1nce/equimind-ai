from fastapi import APIRouter

from app.services.embeddings.embedding_service import EmbeddingService

router = APIRouter()

embedding_service = EmbeddingService()


@router.get("/embedding/test", tags=["Embeddings"])
def test_embedding():

    text = "Apple generated record revenue in fiscal year 2025."

    vector = embedding_service.embed(text)

    return {
        "dimensions": len(vector),
        "first_values": vector[:10],
    }