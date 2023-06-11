import os
import logging
import logging.handlers
from config import Config


LOG_FORMAT = "%(asctime)s [%(levelname)-8s] - %(name)8s.(%(lineno)3d) - %(message)s"
DATE_FMT = "%Y/%m/%d %H:%M:%S"


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FMT))
    return stream_handler


def get_file_handler(log_file: str):
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=log_file, when="d", interval=1, backupCount=0
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FMT))
    return file_handler


def get_log_path_file(cfg: Config) -> tuple:
    return (
        cfg.get_config_value("logging", "path"),
        cfg.get_config_value("logging", "filename"),
    )


def get_log_strategy(cfg: Config) -> int:
    strategies = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }
    return strategies.get(
        cfg.get_config_value("logging", "level").lower(), logging.INFO
    )


def should_log_to_console(cfg: Config) -> bool:
    return cfg.get_config_value("logging", "to_console")


def should_log_to_file(cfg: Config) -> bool:
    return cfg.get_config_value("logging", "to_file")


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    conf = Config()
    logger.setLevel(get_log_strategy(conf))

    if should_log_to_console(conf):
        logger.addHandler(get_stream_handler())

    if should_log_to_file(conf):
        log_path, log_filename = get_log_path_file(conf)

        if not os.path.exists(log_path):
            if conf.get_config_value("logging", "create_folder"):
                os.makedirs(log_path, exist_ok=True)
            else:
                print("Logging folder not found. Exiting...")
                exit(-1)

        logger.addHandler(get_file_handler(os.path.join(log_path, log_filename)))

    return logger
