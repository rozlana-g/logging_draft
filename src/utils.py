import logging
import sys

from src.config import log_formatter


def configure_logger(logger):
    """
    Вообще,
        Child loggers propagate messages up to the handlers associated with their ancestor loggers.
        Because of this, it is unnecessary to define and configure handlers for all the loggers an application uses.
        It is sufficient to configure handlers for a top-level logger and create child loggers as needed.
        (You can, however, turn off propagation by setting the propagate attribute of a logger to False.)
    Но так как я не хочу чтобы логи детей записывались туда же куда и лог главного логгера, то я ставлю proagate=False и
    настраиваю их заново.

    :param logger:
    :return:
    """

    logger.propagate = False
    logger.handlers.clear()  # строчка не нужна если я только в одном месте делаю setup_applevel_logger(logger_name=APP_LOGGER_NAME)?

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(log_formatter)
    logger.addHandler(sh)

    # file with current logs
    fh = logging.FileHandler(f"logs/{logger.name}.log", mode='w')
            # потому что handler-ы не наследуются от логгеров-родителей когда propagate=False,
            #       да и название файла было бы другое
    fh.setFormatter(log_formatter)
    logger.addHandler(fh)

    # file with all the historical logs
    fh = logging.FileHandler(f"history_logs/{logger.name}.log", mode='a')
    fh.setFormatter(log_formatter)
    logger.addHandler(fh)
    return logger
