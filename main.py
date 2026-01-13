from pathlib import Path
import sys
from pipeline.scam_detector.detector import ScamDetector
from utils import get_logger, load_file

#Path normalization
project_root = Path(__file__).parent
sys.path.append(str(project_root))
logger = get_logger(__name__)

def main():
    """
    Main function to run the scam detection pipeline.
    """
    detector = ScamDetector()
    test_message = input("Enter the message to analyze for scams: ")

    try:
        logger.info("Starting scam detection...")
        result = detector.detect_scams(test_message)
        print("Scam Detection Result:", result)
        logger.info("Scam detection completed.")
    except Exception as e:
        logger.error(f"An error occurred during scam detection: {e}")
        print("An error occurred. Please check the logs for details.")


if __name__ == "__main__":
    main()