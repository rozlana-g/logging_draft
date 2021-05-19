import logging
import pathlib
import sys

from src.config import APP_LOGGER_NAME, LOGGING_LEVEL


def get_logger(name):
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(LOGGING_LEVEL)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(module)s - %(funcName)s - "
                                  "%(lineno)d - %(levelname)s - %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()  # строчка не нужна если я только в одном месте делаю setup_applevel_logger(logger_name=APP_LOGGER_NAME)?
    logger.addHandler(sh)

    # file with current logs
    fh = logging.FileHandler(f"logs/{logger.name}.log", mode='w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # file with all the historical logs
    fh = logging.FileHandler(f"history_logs/{logger.name}.log", mode='a')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
