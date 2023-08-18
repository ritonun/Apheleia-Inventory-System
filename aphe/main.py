from log import logger
from database import DatabaseInterface
from component import Component
from settings import db_path


if __name__ == '__main__':
    logger.info('--- START OF PROGRAM ---')

    db = DatabaseInterface(path=db_path)
    db.print_table()
    db.quit()

    logger.info('--- END OF PROGRAM ---\n')
