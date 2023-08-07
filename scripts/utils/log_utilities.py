# set logs
import datetime
import functools
import logging
import os
import json
import requests
import time
import glob

from .file_utilities import get_path
from .credentials_utilities import get_env_variable

PATH = get_path()


def delete_old_logs(days: int = 1):
    folder_path = f"{PATH}/../../logs/"
    current_time = time.time()
    for file_path in glob.glob(os.path.join(folder_path, "*.log")):
        # Get the file's creation time
        creation_time = os.path.getctime(file_path)

        # Calculate the time difference in seconds
        time_difference = current_time - creation_time

        if time_difference >= days * 24 * 60 * 60:  # 2 days in seconds
            # Delete the file
            os.remove(file_path)
            logger.warning(f"Deleted: {file_path}")


def set_basic_logs():
    date = datetime.datetime.now().strftime("%Y%m%d%H%M")
    project_name = PATH.split("/")[-3]
    LOGGING_FORMAT = os.environ.get(
        "LOGGING_FORMAT",
        "[%(asctime)s][%(pathname)s:%(lineno)d][%(levelname)s] - %(message)s",
    )
    LOGGING_FILE = os.environ.get(
        "LOGGING_FILE", f"{PATH}/../../logs/script_{project_name}-{date}.log"
    )
    logging.basicConfig(
        filename=f"{LOGGING_FILE}", level=logging.INFO, format=LOGGING_FORMAT
    )
    delete_old_logs()


set_basic_logs()
logger = logging.getLogger(__name__)


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished executing {func.__name__}")
        return result

    return wrapper


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.warning(
            f"Function {func.__name__} took {end_time - start_time} seconds to run."
        )
        return result

    return wrapper


def teams_on_failure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        webhook_url = get_env_variable("TEAMS_WEBHOOK_URL")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # Send an alert to Microsoft Teams
            message = {
                "title": "Function failed!",
                "text": f"Function '{func.__name__}' has failed with error: {str(e)}",
            }
            response = requests.post(
                webhook_url,
                data=json.dumps(message),
                headers={"Content-Type": "application/json"},
            )
            if response.status_code != 200:
                print(
                    f"Request to Microsoft Teams returned an error {response.status_code}, {response.text}"
                )
            else:
                print("Alert sent to Microsoft Teams")
            raise

    return wrapper


def slack_on_failure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        webhook_url = get_env_variable("SLACK_WEBHOOK_URL")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # Send an alert to Slack
            message = {
                "text": f"Function '{func.__name__}' has failed with error: {str(e)}",
            }
            response = requests.post(
                webhook_url,
                data=json.dumps(message),
                headers={"Content-Type": "application/json"},
            )
            if response.status_code != 200:
                print(
                    f"Request to Slack returned an error {response.status_code}, {response.text}"
                )
            else:
                print("Alert sent to Slack")
            raise

    return wrapper
