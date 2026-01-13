from typing import List,Dict,Any
from utils import get_logger
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt

#Logger
logger = get_logger(__name__)

class ScamDetector:
    """
    A class to detect scams in messages.
    """

    def __init__(self,strategy: str = "react"):
        """
        Initializes the ScamDetector with necessary configurations.
        """
        logger.info("ScamDetector initialized.")
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"Using strategy: {self.strategy}")

    def detect_scams(self, message: str) -> Dict[str, Any]:
        """
        Runs the main scam detection pipeline.
         """
        logger.info("Building prompt for scam detection.")

        try:
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_output = self.parser.parse_llm_output(raw_response)
            logger.info("Scam detection pipeline completed successfully.")
            return parsed_output
        except Exception as e:
            logger.error(f"Error in scam detection pipeline: {e}")
            raise
        