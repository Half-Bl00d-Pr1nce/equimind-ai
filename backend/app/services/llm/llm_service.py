import logging

from google import genai

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
3. Answer clearly and professionally.
4. Use bullet points when appropriate.
5. Keep answers concise but informative.
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
        """
        Generate an answer using Gemini.
        """

        logger.info("Preparing prompt for Gemini...")

        prompt = f"""
{self.SYSTEM_PROMPT}

Context:

{context}

Question:

{question}
"""

        logger.info(
            f"Sending request to {self.MODEL_NAME}..."
        )

        response = self.client.models.generate_content(
            model=self.MODEL_NAME,
            contents=prompt,
        )

        logger.info("Gemini response received.")

        return response.text