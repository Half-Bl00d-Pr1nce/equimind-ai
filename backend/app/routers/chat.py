from fastapi import APIRouter

from app.services.pipeline.chat_pipeline import ChatPipeline

router = APIRouter()

pipeline = ChatPipeline()


@router.get("/chat/{ticker}", tags=["Chat"])
def chat(
    ticker: str,
    question: str,
):
    
    return pipeline.answer(
        ticker,
        question,
    )