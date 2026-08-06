import logging

logger = logging.getLogger(__name__)

class ChunkService:
    """
    Responsible for splitting cleaned
    documents into chunks.
    """

    def embed_chunks(
        self,
        chunks,
    ):
        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        BATCH_SIZE = 20
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

        logger.info(
            "Finished generating embeddings."
        )

        return embeddings