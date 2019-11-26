import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS orders (
            id integer PRIMARY KEY,
            deadline text,
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

    def insert(
        self, deadline, supplier, shipper, customer, sku, item_name, quantity, price
    ):
        self.cur.execute(
            "INSERT INTO orders VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
            (deadline, supplier, shipper, customer, sku, item_name, quantity, price),
        )
        self.con.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM orders WHERE id=?", (id,))
        self.con.commit()

    def update(
        self, id, deadline, supplier, shipper, customer, sku, item_name, quantity, price
    ):
        self.cur.execute(
            """
            UPDATE orders SET
                deadline = ?,
                supplier = ?,
                shipper = ?,
                customer = ?,
                sku = ?,
                item_name = ?,
                quantity = ?,
                price = ?
                WHERE id = ?
            """,
            (
                deadline,
                supplier,
                shipper,
                customer,
                sku,
                item_name,
                quantity,
                price,
                id,
            ),
        )
        self.con.commit()

    def __del__(self):
        self.con.close()


# db = Database("store.db")
# db.insert(
#     "12-03-2019",
#     "IT-Partner Ltd.",
#     "PEC Ltd.",
#     "Kalynkin",
#     "20007",
#     "PSU Cheefteck [550-PNRI]",
#     "2",
#     "2500.00",
# )
# db.insert(
#     "12-03-2019",
#     "Resource Media Ltd.",
#     "Baltic Cargo Ltd.",
#     "TN-Service Ltd.",
#     "56983",
#     "Drum Unit Brother DR-2375 (original)",
#     "1",
#     "12750.00",
# )
# db.insert(
#     "12-03-2019",
#     "Merlion Ltd.",
#     "Business Lines Ltd.",
#     "Real Plus Ltd.",
#     "60534",
#     "HDD Seagate ST1005 SeaWolf 10Gb 10RPM",
#     "10",
#     "120300.00",
# )
