import logging
import sys

from src.config import LOGGING_LEVEL
from src import utils

logger = logging.getLogger('src')
logger.setLevel(LOGGING_LEVEL)
utils.configure_logger(logger)


logger.info('------------------------- NEW RUN --------------------------------------')

from src import module

logger.debug('Calling module function.')
try:
    module.multiply(5, 0)
    logger.debug('Finished.')
except Exception as ex:
    logger.exception(ex)
