import logging

from google import genai
from google.genai.errors import ClientError

from app.core.config import settings

logger = logging.getLogger(__name__)


class LLMService:
    """
    Handles all interactions with the Gemini LLM.
    """

    MODEL_NAME = "gemini-3.6-flash"

    SYSTEM_PROMPT = """
You are an expert Equity Research Analyst.

Your job is to answer questions ONLY using the provided SEC filing context.

Rules:
1. Never make up information.
2. If the answer is not found in the context, say:
   "I could not find this information in the filing."
3. If the answer is spread across multiple retrieved sections,
   combine them into one coherent answer.
4. Keep answers professional, concise and well structured.
"""

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

        logger.info("LLMService initialized.")

    def answer(
        self,
        question: str,
        context: str,
    ):

        logger.info("Preparing prompt for Gemini...")

        prompt = f"""
{self.SYSTEM_PROMPT}

Context:

{context}

Question:

{question}
"""

        try:

            response = self.client.models.generate_content(
                model=self.MODEL_NAME,
                contents=prompt,
            )

            logger.info("Gemini response received.")

            return response.text

        except ClientError as e:

            logger.exception("Gemini API error")

            if getattr(e, "code", None) == 429:
                return (
                    "⚠️ The AI service has temporarily reached its free-tier "
                    "request limit. Please wait a minute and try again."
                )

            return (
                "⚠️ An error occurred while generating the response. "
                "Please try again later."
            )

        except Exception:

            logger.exception("Unexpected LLM error")

            return (
                "⚠️ Unexpected server error while generating the answer."
            )