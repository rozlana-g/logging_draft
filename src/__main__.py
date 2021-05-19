import logging
import sys

from src.config import LOGGING_LEVEL
from src import utils

logger = utils.get_logger('src')

from src import module

logger.debug('Calling module function.')
try:
    module.multiply(5, 0)
    logger.debug('Finished.')
except Exception as ex:
    logger.exception(ex)
