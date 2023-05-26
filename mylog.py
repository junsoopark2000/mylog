import os
import sys
import logging
import logging.handlers
from dotenv import load_dotenv

DEFAULT_LOG_FILE = "./default.log"

_log_format = "%(asctime)s [%(levelname)8s] - %(name)8s.(%(lineno)3d) - %(message)s"

# Load environment variables from .env file
load_dotenv()

# Define log levels
log_level_in_environment = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

# Get the log level from the environment variable or set it to INFO by default
_logger_level = log_level_in_environment.get(os.getenv("LOG_LEVEL"), logging.INFO)

# Get the log file path and name from the environment variable
_filename = os.getenv("LOG_PATH_AND_FILENAME")

if _filename is None:
    print(
        f"LOG_PATH_AND_FILENAME is NOT DEFINED. set to default log path and file{DEFAULT_LOG_FILE}"
    )
    _filename = DEFAULT_LOG_FILE

_file_handler_level = logging.DEBUG
_stream_handler_level = logging.DEBUG


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(_stream_handler_level)
    stream_handler.setFormatter(
        logging.Formatter(_log_format, datefmt="%Y/%m/%d %H:%M:%S")
    )
    return stream_handler


def get_file_handler():
    file_handler = logging.handlers.TimedRotatingFileHandler(
        _filename, when="h", interval=1, backupCount=0
    )
    file_handler.setLevel(_file_handler_level)
    file_handler.setFormatter(
        logging.Formatter(_log_format, datefmt="%Y/%m/%d %H:%M:%S")
    )
    return file_handler


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(_logger_level)
    logger.addHandler(get_stream_handler())
    logger.addHandler(get_file_handler())
    return logger
