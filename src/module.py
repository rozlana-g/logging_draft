from src import utils

logger = utils.get_logger(__name__)
logger.info('------------------------- NEW RUN --------------------------------------')


def multiply(num1, num2): # just multiply two numbers
    logger.debug("Executing multiply function.")
    return num1 / num2

# multiply(5, 1)