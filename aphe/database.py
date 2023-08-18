import sqlite3
from component import Component


class DatabaseInterface:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""CREATE TABLE inventory(
            name text,
            category text,
            quantity integer
            )""")

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


if __name__ == '__main__':
    db = DatabaseInterface()
    db.create_table()

    comp1 = Component("100k", "Resistor")
    comp2 = Component("UNO", "Arduino")

    db.insert_component(comp1, 10)
    db.insert_component(comp2, 1)

    db.show_table()

    db.update_quantity(comp1, 5)
    db.operation_quantity(comp2, -2)

    db.show_table()
