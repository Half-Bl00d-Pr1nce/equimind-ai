import logging

from app.services.embeddings.embedding_service import EmbeddingService
from app.services.llm.llm_service import LLMService
from app.services.vector_db.qdrant_service import QdrantService

logger = logging.getLogger(__name__)


class ChatPipeline:
    """
    End-to-end question answering pipeline.
    """

    def __init__(self):

        self.embedding = EmbeddingService()
        self.qdrant = QdrantService()
        self.llm = LLMService()

    def answer(
        self,
        ticker: str,
        question: str,
    ):
        """
        Answer a user question using indexed SEC filings.
        """

        logger.info(f"Starting chat pipeline for {ticker.upper()}")

        # Generate embedding
        query_embedding = self.embedding.embed(question)

        # Retrieve relevant chunks
        chunks = self.qdrant.search(
            ticker,
            query_embedding,
        )

        logger.info(f"Retrieved {len(chunks)} chunks")

        context = "\n\n".join(chunks)

        # Generate final answer
        answer = self.llm.answer(
            question,
            context,
        )

        logger.info("Answer generated successfully.")

        return {
            "company": ticker.upper(),
            "question": question,
            "answer": answer,
            "sources_used": len(chunks),
            "model": self.llm.MODEL_NAME,
        }