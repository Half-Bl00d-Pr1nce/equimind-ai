import logging

from google import genai
from app.config.settings import settings

logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    Generates embeddings using Gemini.
    """

    MODEL_NAME = "gemini-embedding-001"

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    def embed(
        self,
        text: str,
    ):

        response = self.client.models.embed_content(
            model=self.MODEL_NAME,
            contents=text,
        )

        return response.embeddings[0].values

    def embed_chunks(
        self,
        chunks,
    ):

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        embeddings = []

        for chunk in chunks:

            response = self.client.models.embed_content(
                model=self.MODEL_NAME,
                contents=chunk,
            )

            embeddings.append(
                response.embeddings[0].values
            )

        logger.info(
            "Finished generating embeddings."
        )

        return embeddings