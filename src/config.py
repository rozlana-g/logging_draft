import logging

APP_LOGGER_NAME = 'My_App'
LOGGING_LEVEL = logging.DEBUG
log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(module)s - %(funcName)s - "
                              "%(lineno)d - %(levelname)s - %(message)s")