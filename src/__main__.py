import logging
import sys

from src.config import LOGGING_LEVEL, log_formatter

logger = logging.getLogger('src')
logger.setLevel(LOGGING_LEVEL)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(log_formatter)
logger.handlers.clear()  # строчка не нужна если я только в одном месте делаю setup_applevel_logger(logger_name=APP_LOGGER_NAME)?
logger.addHandler(sh)

logger.info('------------------------- NEW RUN --------------------------------------')

from src import module

logger.debug('Calling module function.')
try:
    module.multiply(5, 0)
    logger.debug('Finished.')
except Exception as ex:
    logger.exception(ex)
