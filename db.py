import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXIST orders (
            id integer PRIMARY KEY,
            supplier text,
            shipper text,
            customer text,
            sku integer,
            item_name text,
            quantity real,
            price real
            )"""
        )
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM orders")
        rows = self.cur.fetchall()
        return rows

    def insert(self, supplier, shipper, customer, sku, item_name, quantity, price):
        self.cur.execute(
            "INSERT INTO orders VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
            (supplier, shipper, customer, sku, item_name, quantity, price),
        )
        self.con.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM orders WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, supplier, shipper, customer, sku, item_name, quantity, price):
        self.cur.execute(
            """
            UPDATE orders SET
                supplier = ?,
                shipper = ?,
                customer = ?,
                sku = ?,
                item_name = ?,
                quantity = ?,
                price = ?
                WHERE id = ?
            """,
            (supplier, shipper, customer, sku, item_name, quantity, price, id),
        )
        self.con.commit()

    def __del__(self):
        self.con.close()
