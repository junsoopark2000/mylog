import logging
import logging.handlers

_log_format = f"%(asctime)s - [%(levelname)8s] - %(name)8s.(%(lineno)3d) - %(message)s"
_logger_level = logging.DEBUG
_handler_level = logging.CRITICAL  # for both stream_handler, file_handler
_filename = "app.log"


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(_handler_level)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_file_handler():
    file_handler = logging.handlers.RotatingFileHandler("app.log", maxBytes=1024, backupCount=5)
    file_handler = logging.handlers.TimedRotatingFileHandler(
        _filename, when="m", interval=2, backupCount=0
    )  # roll over every two minutes
    file_handler.setLevel(_handler_level)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(_logger_level)
    logger.addHandler(get_stream_handler())
    logger.addHandler(get_file_handler())
    return logger
