# -*- coding: utf-8 -*

import sqlite3 as sqlite


class Table:
    def __init__(self, table="Tables", database="templates/db/database.db"):
        self.table = table
        self.database = database

    def get_all_db_data(self):
        db = sqlite.connect(self.database)
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()
            conn.execute("SELECT * FROM {}".format(self.table))
            data = conn.fetchall()

            return data

    def init_table(self):
        db = sqlite.connect(self.database)
        with db:
            conn = db.cursor()

            conn.execute("CREATE TABLE {} (id INTEGER, employeeId INTEGER, month INTEGER, year INTEGER, hours TEXT)".format(self.table))
            db.commit()

            tables = (
                (1, 1, 1, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (2, 1, 2, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (3, 1, 3, 2015, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (4, 1, 4, 2015, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (5, 1, 5, 2015, u"8 в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (6, 1, 6, 2015, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (7, 1, 7, 2015, u"в в 8 8 9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (8, 1, 8, 2015, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (9, 1, 9, 2015, u"в в 8 8 8 8 10 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (10, 1, 10, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (11, 1, 11, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (12, 1, 12, 2016, u"в в 8 8 8 8 8 5 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (13, 2, 1, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (14, 2, 2, 2016, u"в в 8 8 8 8 8 8 4 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (15, 2, 3, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (16, 2, 4, 2016, u"в в 8 8 8 8 8 8 8 8 8 2 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (17, 2, 5, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (18, 2, 6, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (19, 2, 7, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (20, 2, 8, 2016, u"в в 8 8 8 8 8 8 8 8 8 8 1 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (21, 2, 9, 2015, u"в в 8 8 8 8 8 8 8 8 8 8 б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (22, 2, 10, 2015, u"в в 8 8 8 8 8 8 8 б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (23, 2, 11, 2015, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (24, 2, 12, 2015, u"в в 8 8 8 8 8 8 6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (25, 3, 1, 2017, u"в в 8 8 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (26, 3, 2, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (27, 3, 3, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 0 8 8 8 8 8 8 8 8 8 8 8 8"),
                (28, 3, 4, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1 8 8 8 8 8 8 8 8 8 8 8 8"),
                (29, 3, 5, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 7 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (30, 3, 6, 2017, u"в в 8 8 8 8 8 8 8 8 8 6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (31, 3, 7, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (32, 3, 8, 2017, u"в в 8 8 8 8 8 8 8 б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (33, 3, 9, 2016, u"в в в в в в в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (34, 3, 10, 2016, u"б б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (35, 3, 11, 2016, u"б б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (36, 3, 12, 2016, u"б б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (37, 4, 1, 2017, u"в в 8 8 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (38, 4, 2, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (39, 4, 3, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 0 8 8 8 8 8 8 8 8 8 8 8 8"),
                (40, 4, 4, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1 8 8 8 8 8 8 8 8 8 8 8 8"),
                (41, 4, 5, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 7 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (42, 4, 6, 2017, u"в в 8 8 8 8 8 8 8 8 8 6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (43, 4, 7, 2017, u"в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (44, 4, 8, 2017, u"в в 8 8 8 8 8 8 8 б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (45, 4, 9, 2016, u"в в в в в в в в 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (46, 4, 10, 2016, u"б б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (47, 4, 11, 2016, u"б б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (48, 4, 12, 2016, u"б б 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8")
            )

            conn.executemany("INSERT INTO {} (id, employeeId, month, year, hours) VALUES (?, ?, ?, ?, ?)".format(self.table), tables)
            db.commit()