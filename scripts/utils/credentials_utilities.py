import os

import boto3
from airflow.models import Variable
from google.oauth2 import service_account
from google.cloud import bigquery
from airflow.models import Variable
from google.cloud import storage

import json


def get_env_variable(var_name: str) -> str:
    """Try to get variable from environment, if not found, get from Airflow Variables"""
    creds_var = os.environ.get(var_name, Variable.get(var_name))

    return creds_var


def set_boto3_session() -> None:
    aws_access_key_id = get_env_variable("ACCESS_KEY_ID")
    aws_secret_access_key = get_env_variable("SECRET_ACCESS_KEY")
    region_name = "us-east-2"

    boto3.setup_default_session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name,
    )


def get_bigquery_client(var_name: str) -> bigquery.Client:
    creds_var = get_env_variable(var_name)
    creds_dict = json.loads(creds_var)

    CREDS = service_account.Credentials.from_service_account_info(creds_dict)
    client = bigquery.Client(credentials=CREDS, project=CREDS.project_id)

    return client


def get_storage_client(var_name: str) -> storage.Client:
    creds_var = get_env_variable(var_name)
    creds_dict = json.loads(creds_var)

    CREDS = service_account.Credentials.from_service_account_info(creds_dict)
    client = storage.Client(credentials=CREDS, project=CREDS.project_id)

    return client
