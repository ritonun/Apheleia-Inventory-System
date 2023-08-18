from log import logger
from database import DatabaseInterface
from component import Component


if __name__ == '__main__':
    logger.info('--- START OF PROGRAM ---')
    db = DatabaseInterface()

    comp1 = Component("100k", "Resistor")
    comp2 = Component("UNO", "Arduino")

    db.insert_component(comp1, 10)
    db.insert_component(comp2, 1)

    db.show_table()

    db.update_quantity(comp1, 5)
    db.operation_quantity(comp2, -2)

    db.show_table()

    db.quit()
    logger.info('--- END OF PROGRAM ---\n')
