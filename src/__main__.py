
from src import utils

logger = utils.configure_logger('src')



logger.info('------------------------- NEW RUN --------------------------------------')

from src import module

logger.debug('Calling module function.')
try:
    module.multiply(5, 0)
    logger.debug('Finished.')
except Exception as ex:
    logger.exception(ex)
