import logging

from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    Singleton embedding service.
    """

    MODEL_NAME = "all-MiniLM-L6-v2"

    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def _load_model(self):
        if self._model is None:
            logger.info(
                f"Loading embedding model '{self.MODEL_NAME}'..."
            )

            self._model = SentenceTransformer(
                self.MODEL_NAME
            )

            logger.info(
                "Embedding model loaded successfully."
            )

    def embed(self, text: str):

        self._load_model()

        embedding = self._model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_chunks(self, chunks):

        self._load_model()

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        embeddings = self._model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True,
            batch_size=8,
            show_progress_bar=True,
        )

        logger.info(
            "Finished generating embeddings."
        )

        return embeddings.tolist()