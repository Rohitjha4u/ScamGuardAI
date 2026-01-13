"""
LLM Client for Google Gemini API interactions with retry logic and incremental delay.
"""
import time
from google import genai
from config import GEMINI_API_KEY, DEFAULT_MODEL, MAX_RETRIES, RETRY_DELAY
from utils import get_logger

# Logger
logger = get_logger(__name__)

class LLMClient:
    """
    A client to interact with the Google Gemini API with retry logic.
    """

    def __init__(self, model_name=DEFAULT_MODEL,max_retries=MAX_RETRIES, retry_delay=RETRY_DELAY):
        """
        Initializes the LLMClient with API key and model.
        """
        self.model_name = model_name or DEFAULT_MODEL
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.client = genai.Client(api_key=GEMINI_API_KEY)


    def generate_response(self, prompt: str, **kwargs) -> str:
        """
        Generates a response from the Gemini API with retry logic.
        """
        if not self.model_name:
            raise ValueError("Model name is not set. Please provide a valid model name.")

        for attempt in range(self.max_retries):
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                    **kwargs
                )

                if response and response.text:
                    return response.text.strip()
                else:
                    raise ValueError("Empty response from Gemini API.")

            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))
                else:
                    logger.error("Max retries reached. Raising exception.")
                    raise 
        
        # Fallback in case max_retries is 0 or loop is skipped
        raise RuntimeError("Unexpected error: Retry loop finished without result.")