class ChunkService:
    """
    Responsible for splitting cleaned
    documents into chunks.
    """

    def chunk(
        self,
        text: str,
        chunk_size: int = 1500,
        overlap: int = 300,
    ):
        """
        Split text into overlapping chunks.
        """

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(text[start:end])

            start += chunk_size - overlap

        return chunks