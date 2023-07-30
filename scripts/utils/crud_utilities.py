"""This file contains the CRUD utilities for the application, such as the ones which involve the database."""
from contextlib import contextmanager
import pandas as pd
import psycopg2
from .credentials_utilities import get_env_variable
import logging

logger = logging.getLogger(__name__)


@contextmanager
def get_redshift_conn() -> psycopg2.connect:
    try:
        cnx = psycopg2.connect(
            dbname=get_env_variable("DB_NAME"),
            user=get_env_variable("DB_USER"),
            password=get_env_variable("REDSHIFT_PASS"),
            host=get_env_variable("REDSHIFT_HOST"),
            port=5439,
        )
        yield cnx
    finally:
        cnx.close()


def execute_query(query: str):
    with get_redshift_conn() as cnx:
        with cnx.cursor() as cur:
            cur.execute(query)
            cnx.commit()


def delete(query: str) -> None:
    try:
        execute_query(query)
        logger.info("Deleted data.")
    except Exception as e:
        logger.info(f"Error deleting data: {e}")


def insert(query: str) -> None:
    try:
        execute_query(query)
        logger.info("Inserted data.")
    except Exception as e:
        logger.info(f"Error inserting data: {e}")


def update(query: str) -> None:
    try:
        execute_query(query)
        logger.info("Updated data.")
    except Exception as e:
        logger.info(f"Error updating data: {e}")


def select(query: str) -> pd.DataFrame:
    try:
        df = pd.read_sql(query, con=get_redshift_conn())
        logger.info("Selected data.")
        return df
    except Exception as e:
        logger.info(f"Error selecting data: {e}")
