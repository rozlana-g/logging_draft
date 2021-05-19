from src import utils
from src import module

logger = utils.get_logger('src')
logger.info('------------------------- NEW RUN --------------------------------------')

logger.debug('Calling module function.')
try:
    module.multiply(5, 0)
    logger.debug('Finished.')
except Exception as ex:
    logger.exception(ex)
