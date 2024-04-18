import logging

from app.core.config import settings


# NOTE: db logger can also be added for checking the query performance and all
def setup_loggers():
    # Root Logger
    logging.basicConfig(level=logging.INFO, filename=f'{settings.LOG_DIR}/app.log', filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Request Logger
    request_logger = logging.getLogger('request')
    request_handler = logging.FileHandler(f'{settings.LOG_DIR}/requests.log')
    request_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    request_logger.addHandler(request_handler)

    # Error Logger
    error_logger = logging.getLogger('error')
    error_handler = logging.FileHandler(f'{settings.LOG_DIR}/errors.log')
    error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    error_logger.addHandler(error_handler)

    # Server Logger
    server_logger = logging.getLogger('server')
    server_handler = logging.FileHandler(f'{settings.LOG_DIR}/server.log')
    server_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    server_logger.addHandler(server_handler)
