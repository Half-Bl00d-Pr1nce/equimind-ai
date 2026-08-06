import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = "EquiMind AI"
    APP_VERSION = "1.0.0"

    GOOGLE_API_KEY = os.getenv(
        "GOOGLE_API_KEY"
    )

    QDRANT_URL = os.getenv(
        "QDRANT_URL"
    )

    QDRANT_API_KEY = os.getenv(
        "QDRANT_API_KEY"
    )


settings = Settings()