import logging

from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    Generates embeddings using Sentence Transformers.
    """

    MODEL_NAME = "all-MiniLM-L6-v2"

    def __init__(self):

        logger.info(
            f"Loading embedding model '{self.MODEL_NAME}'..."
        )

        self.model = SentenceTransformer(
            self.MODEL_NAME
        )

        logger.info(
            "Embedding model loaded successfully."
        )

    def embed(
        self,
        text: str,
    ):

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_chunks(
        self,
        chunks,
    ):

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True,
            batch_size=32,
            show_progress_bar=True,
        )

        logger.info(
            "Finished generating embeddings."
        )

        return embeddings.tolist()