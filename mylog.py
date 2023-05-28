"""
My log library
"""
import os
import logging
import logging.handlers
from dotenv import load_dotenv


DEFAULT_LOG_FILE = "./default.log"
LOG_FORMAT = "%(asctime)s [%(levelname)-8s] - %(name)8s.(%(lineno)3d) - %(message)s"
DATE_FMT = "%Y/%m/%d %H:%M:%S"


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
    path_and_filename: str = os.getenv("LOG_PATH_AND_FILENAME")
    return DEFAULT_LOG_FILE if path_and_filename is None else path_and_filename


def get_log_level_in_config() -> int:
    """Returns: logging.DEBUG | logging.INFO | logging.WARNING | logging.ERROR | logging.CRITICAL"""
    load_dotenv()
    log_strategies = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    return log_strategies.get(os.getenv("LOG_LEVEL").upper(), logging.INFO)


def get_logger(name: str) -> logging.Logger:
    """returns a logger for each module(.py)"""
    logger = logging.getLogger(name)
    logger.setLevel(get_log_level_in_config())
    logger.addHandler(get_stream_handler())
    logger.addHandler(get_file_handler())
    return logger
