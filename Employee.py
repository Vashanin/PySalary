# -*- coding: utf-8 -*

import sqlite3 as sqlite

class Employee:
    def __init__(self, table="Employees", database="templates/db/database.db"):
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
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()
            employees = (
                (1, u"Анакинов Владислав Петрович", "HR"),
                (2, u"Голованов Сергй Дмитрович", "Team Lead"),
                (3, u"Адамовський Анатолій Ростиславович", "Software Tester"),
                (4, u"Куршаков Дмитро Владиславович", "Middle Python Developer")
            )
            conn.execute("DROP TABLE {}".format(self.table))
            db.commit()

            conn.execute("CREATE TABLE {} (id INTEGER, name TEXT, post TEXT)".format(self.table))
            db.commit()

            conn.executemany("INSERT INTO {} (id, name, post) VALUES (?, ?, ?)".format(self.table), employees)
            db.commit()