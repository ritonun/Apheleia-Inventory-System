import logging
from settings import log_file_path

# Logger LEVEL:
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

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
