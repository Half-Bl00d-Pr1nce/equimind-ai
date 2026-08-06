import logging
import time
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
        """
        Generate embeddings in batches to avoid
        Gemini rate limits.
        """

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        BATCH_SIZE = 10

        embeddings = []

        for i in range(0, len(chunks), BATCH_SIZE):

            batch = chunks[i:i + BATCH_SIZE]

            response = self.client.models.embed_content(
                model=self.MODEL_NAME,
                contents=batch,
            )

            embeddings.extend(
                [
                    embedding.values
                    for embedding in response.embeddings
                ]
            )

            time.sleep(3)

            logger.info(
                f"Embedded {min(i + BATCH_SIZE, len(chunks))}/{len(chunks)} chunks"
            )

        logger.info(
            "Finished generating embeddings."
        )

        return embeddings