"""
My log library
"""
import os
import logging
import logging.handlers
from dotenv import load_dotenv


DEFAULT_LOG_PATH = "./"
LOG_FILE_NAME = "app.log"
LOG_FORMAT = "%(asctime)s [%(levelname)-8s] - %(name)8s.(%(lineno)3d) - %(message)s"
DATE_FMT = "%Y/%m/%d %H:%M:%S"

load_dotenv()


def get_stream_handler():
    """returns a stream handler"""
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FMT))
    return stream_handler


def get_file_handler():
    """returns a file handler"""
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=get_log_path_file(), when="d", interval=1, backupCount=0
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FMT))
    return file_handler


def get_log_path_file() -> str:
    """get log path and filename"""

    log_path: str = os.getenv("LOG_PATH")

    if log_path is None or not log_path:  # undefined or empty string
        log_path = os.getcwd()

    elif not os.path.exists(log_path):
        os.makedirs(log_path, exist_ok=True)

    return f"{log_path}/{LOG_FILE_NAME}"


def get_log_level_in_config() -> int:
    """Returns: logging.DEBUG | logging.INFO | logging.WARNING | logging.ERROR | logging.CRITICAL"""

    log_strategies = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    return log_strategies.get(os.getenv("LOG_LEVEL").lower(), logging.INFO)


def get_logger(name: str) -> logging.Logger:
    """returns a logger for each module(.py)"""

    logger = logging.getLogger(name)
    logger.setLevel(get_log_level_in_config())

    if os.getenv("LOG_PRINT_ON_FILE").lower() == "true":
        logger.addHandler(get_file_handler())

    if os.getenv("LOG_PRINT_ON_CONSOLE").lower() == "true":
        logger.addHandler(get_stream_handler())

    return logger
