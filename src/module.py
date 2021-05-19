import logging

from src import utils

logger = logging.getLogger(__name__)
utils.configure_logger(logger)

logger.info('------------------------- NEW RUN --------------------------------------')


def multiply(num1, num2): # just multiply two numbers
    logger.debug("Executing multiply function.")
    return num1 / num2

# multiply(5, 1)