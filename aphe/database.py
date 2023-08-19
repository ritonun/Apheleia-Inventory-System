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
            value text,
            category text,
            quantity integer
            )""")
        logger.info("Created table \'inventory\'")

    def execute(self, query, data):
        with self.conn:
            self.cur.execute(query, data)

    def insert_component(self, comp, quantity):
        with self.conn:
            self.cur.execute("INSERT INTO inventory VALUES (:value, :category, :quantity)",
                        {"value": comp.value, "category": comp.category, "quantity": quantity})

    def update_quantity(self, value, category, quantity):
        with self.conn:
            self.cur.execute("""UPDATE inventory SET quantity=:quantity
                                WHERE value=:value AND category=:category""",
                                {"value": value, "category": category, "quantity": quantity})

    def operation_quantity(self, value, category, number):
        self.cur.execute("SELECT * FROM inventory WHERE value=:value AND category=:category", 
                            {"value": value, "category": category})
        quantity = self.cur.fetchone()[2]
        with self.conn:
            self.cur.execute("""UPDATE inventory SET quantity=:quantity
                                WHERE value=:value AND category=:category""",
                                {"value": value, "category": category, "quantity": quantity + number})

    def fetch_all_table(self):
        self.cur.execute("SELECT * FROM inventory")
        table = self.cur.fetchall()
        return table

    def print_table(self):
        self.cur.execute("SELECT * FROM inventory")
        table = self.cur.fetchall()

        element = []
        length_list = []
        for i in range(len(table[0])):
            element.append([])
            length_list.append([])

        for count, component in enumerate(table):
            for index in range(len(component)):
                element[index].append(str(component[index]))

        for index in range(len(element)):
            length_list[index] = len(max(element[index], key=len))

        separator = " | "

        labels = ["VALUE", "CATEGORY", "QUANTITY"]
        for i in range(len(labels)):
            if length_list[i] < len(labels[i]):
                length_list[i] = len(labels[i])

            end = separator
            if i == len(labels) - 1:
                end = "\n"

            print(labels[i] + " " * (length_list[i] - len(labels[i])), end=end )

        for i in range(len(element[0])):
            for j in range(len(element)):
                end = separator
                if j == len(element) - 1:
                    end = "\n"
                print(element[j][i] + " " * (length_list[j] - len(element[j][i])), end=end)

        return table

    def quit(self):
        self.conn.close()
        logger.info("Database connector close")
