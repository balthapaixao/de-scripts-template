from utils.log_utilities import log_execution, timing_decorator
import logging

logger = logging.getLogger(__name__)


@log_execution
@timing_decorator
def main():
    logger.info("Hello World!")


if __name__ == "__main__":
    main()
