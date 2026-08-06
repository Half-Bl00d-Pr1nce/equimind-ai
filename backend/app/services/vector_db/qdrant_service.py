import logging
import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
    Filter,
    FieldCondition,
    MatchValue,
)
from app.core.config import settings
from qdrant_client.models import PayloadSchemaType

logger = logging.getLogger(__name__)


class QdrantService:
    """
    Handles all interactions with Qdrant.
    """

    COLLECTION_NAME = "sec_filings"

    def __init__(self):

        if settings.QDRANT_API_KEY:
            self.client = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY,
            )
        else:
            self.client = QdrantClient(
                url=settings.QDRANT_URL,
            )

        logger.info("Connected to Qdrant.")

    def create_collection(
        self,
        vector_size: int,
    ):
        """
        Create the collection if it does not already exist.
        """

        logger.info(
            f"Checking collection '{self.COLLECTION_NAME}'."
        )

        collections = self.client.get_collections()

        existing = [
            collection.name
            for collection in collections.collections
        ]

        if self.COLLECTION_NAME in existing:

            logger.info(
                "Collection already exists."
            )

            return

        logger.info(
            "Creating Qdrant collection..."
        )

        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

        self.client.create_payload_index(
            collection_name=self.COLLECTION_NAME,
            field_name="ticker",
            field_schema=PayloadSchemaType.KEYWORD,
        )

        logger.info(
            "Collection created successfully."
        )

    def upload_chunks(
        self,
        ticker: str,
        chunks,
        embeddings,
    ):
        """
        Upload document chunks and embeddings.
        """

        logger.info(
            f"Uploading {len(chunks)} chunks..."
        )

        points = []

        for chunk, embedding in zip(
            chunks,
            embeddings,
        ):

            points.append(

                PointStruct(

                    id=str(uuid.uuid4()),

                    vector=embedding,

                    payload={
                        "ticker": ticker.upper(),
                        "text": chunk,
                    },
                )

            )

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=points,
        )

        logger.info(
            "Upload completed successfully."
        )

    def search(
        self,
        ticker: str,
        query_vector,
        limit: int = 5,
    ):
        """
        Search the vector database.
        """

        logger.info(
            f"Searching top {limit} chunks for {ticker.upper()}..."
        )

        results = self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=query_vector,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="ticker",
                        match=MatchValue(
                            value=ticker.upper()
                        ),
                    )
                ]
            ),
            limit=limit,
        )

        logger.info(
            f"Retrieved {len(results.points)} chunks."
        )

        return [
            point.payload["text"]
            for point in results.points
        ]

    def count_vectors(self):
        """
        Return the number of vectors in the collection.
        """

        info = self.client.get_collection(
            self.COLLECTION_NAME
            
        )

        return info.points_count
    
    def company_vector_count(
        self,
        ticker: str,
    ) -> int:
        """
        Return the number of vectors stored
        for a company.
        """

        result = self.client.count(
            collection_name=self.COLLECTION_NAME,
            count_filter=Filter(
                must=[
                    FieldCondition(
                        key="ticker",
                        match=MatchValue(
                            value=ticker.upper()
                        )
                    )
                ],
            ),
            exact=True,
        )

        return result.count