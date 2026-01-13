from typing import Optional
from llm.client import LLMClient
from utils import get_logger

# Logger
logger = get_logger(__name__)

class LLMExecutor:
    """
    Executor class to interact with the LLM client.
    """

    def __init__(self, model_name: Optional[str] = None):
        """
        Initializes the LLMExecutor with an LLM client.
        """
        self.llm:LLMClient = LLMClient(model_name) if model_name else LLMClient()
        logger.info("LLMExecutor initialized with model: %s", self.llm.model_name)


    def execute(self, prompt: str) -> str:
        """
        Executes the prompt using LLM client and returns raw response.

        Args:
            prompt: The formatted prompt string to send to LLM.
        Returns:
            Raw response from LLM.
        Raises:
            Exception: When LLM call fails.
        """
        logger.info(f"Executing LLM with final prompt")
        try:
            response = self.llm.generate_response(prompt)
            logger.info("LLM execution successful.")
            return response
        except Exception as e:
            logger.error(f"LLM execution failed: {e}")
            raise