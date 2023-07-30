import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_data(df: pd.DataFrame) -> None:
    """
    Extract data
    """
    logger.info("Loading data...")
    df = ...
    logger.info("Data loaded!")
