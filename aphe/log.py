import logging
from settings import log_file_path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(module)s.py: %(levelname)s: %(message)s')

file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def test_level():
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')


if __name__ == '__main__':
    logger.info('--- START OF PROGRAM --- ')
    test_level()
    logger.info('--- END OF PROGRAM --- \n')
