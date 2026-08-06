from pathlib import Path
import logging
from app.services.parser.html_parser import HTMLParser
from app.services.parser.cleaner import DocumentCleaner
from app.services.chunking.chunk_service import ChunkService

logger = logging.getLogger(__name__)


class DocumentPipeline:

    def __init__(self):

        self.parser = HTMLParser()
        self.cleaner = DocumentCleaner()
        self.chunker = ChunkService()

    def process(self, file_path: str):

        logger.info(f"Reading document: {file_path}")

        html = Path(file_path).read_text(
            encoding="utf-8"
        )

        logger.info("Parsing HTML...")
        raw_text = self.parser.parse(html)

        logger.info("Cleaning parsed text...")
        clean_text = self.cleaner.clean(raw_text)

        logger.info("Chunking document...")
        chunks = self.chunker.chunk(clean_text)

        logger.info(f"Generated {len(chunks)} chunks.")

        return chunks