import logging
import sys

from src.config import log_formatter


def get_logger(name):
    logger = logging.getLogger(name)
    logger.propagate = False

    sh = logging.StreamHandler(sys.stdout) # потому что handler-ы не наследуются от логгеров-родителей
    sh.setFormatter(log_formatter)
    logger.addHandler(sh)

    # file with current logs
    fh = logging.FileHandler(f"logs/{logger.name}.log", mode='w') # потому что handler-ы не наследуются от логгеров-родителей,
                                                                    # да и название файла было бы другое
    fh.setFormatter(log_formatter)
    logger.addHandler(fh)

    # file with all the historical logs
    fh = logging.FileHandler(f"history_logs/{logger.name}.log", mode='a')
    fh.setFormatter(log_formatter)
    logger.addHandler(fh)
    return logger
