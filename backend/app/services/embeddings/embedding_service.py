import logging

from fastembed import TextEmbedding

logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    Generates embeddings using FastEmbed.
    """

    MODEL_NAME = "BAAI/bge-small-en-v1.5"

    def __init__(self):

        logger.info(
            f"Loading embedding model '{self.MODEL_NAME}'..."
        )

        self.model = TextEmbedding(
            model_name=self.MODEL_NAME
        )

        logger.info(
            "Embedding model loaded successfully."
        )

    def embed(
        self,
        text: str,
    ):

        embedding = next(
            self.model.embed([text])
        )

        return embedding.tolist()

    def embed_chunks(
        self,
        chunks,
    ):

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        embeddings = []

        for embedding in self.model.embed(chunks):

            embeddings.append(
                embedding.tolist()
            )

        logger.info(
            "Finished generating embeddings."
        )

        return embeddings