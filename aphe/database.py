import sqlite3
import os.path
from log import logger


class DatabaseInterface:
    def __init__(self, path=":memory:"):
        db_exist = self.check_db_exist(path)
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

        if not db_exist:
            self.create_table()

    def check_db_exist(self, path):
        exist = False
        if os.path.isfile(path):
            exist = True
        return exist

    def create_table(self):
        self.cur.execute("""CREATE TABLE inventory(
            name text,
            category text,
            quantity integer
            )""")
        logger.info("Created table \'inventory\'")

    def execute(self, query, data):
        with self.conn:
            self.cur.execute(query, data)

    def insert_component(self, comp, quantity):
        with self.conn:
            self.cur.execute("INSERT INTO inventory VALUES (:name, :category, :quantity)",
                        {"name": comp.name, "category": comp.category, "quantity": quantity})

    def update_quantity(self, comp, quantity):
        with self.conn:
            self.cur.execute("""UPDATE inventory SET quantity=:quantity
                                WHERE name=:name AND category=:category""",
                                {"name": comp.name, "category": comp.category, "quantity": quantity})

    def operation_quantity(self, comp, number):
        self.cur.execute("SELECT * FROM inventory WHERE name=:name", {"name": comp.name})
        quantity = self.cur.fetchone()[2]
        with self.conn:
            self.cur.execute("""UPDATE inventory SET quantity=:quantity
                                WHERE name=:name AND category=:category""",
                                {"name": comp.name, "category": comp.category, "quantity": quantity + number})

    def show_table(self):
        self.cur.execute("SELECT * FROM inventory")
        table = self.cur.fetchall()
        print('VALUE | CATEGORY | QTITY')
        for i in table:
            print(i[0] + " | " + i[1] + " | " + str(i[2]))
        return table

    def quit(self):
        self.conn.close()
        logger.info("Database connector close")
