# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
from Employee import Employee

class Table:
    """
        Клас Table створено для будь-якої взаємодій, що пов'язана з табелями: 
        додання/видалення/редагування, що можна побачити з однойменних методів, 
        які мають доступ до відповідних таблиць всередині баз даних, де зберігається вся інформація
    """

    def __init__(self, table="Tables", database="templates/db/database.db"):
        self.table = table
        self.database = database

    def add_table(self, employee_name, month, year, hours):
        self.add_to_db(employee_name, month, year, hours)

    def remove_table(self, id):
        try:
            db = sqlite.connect(self.database)
            with db:
                conn = db.cursor()
                conn.execute("DELETE FROM {} WHERE id={}".format(self.table, id))
        except Exception as e:
            print(e.args)


    def edit_table(self, id, employee_name, month, year, hours):
        return None
    

    def get_all_db_data(self):
        db = sqlite.connect(self.database)
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()
            conn.execute("SELECT * FROM {}".format(self.table))
            data = conn.fetchall()

            return data

    # функція init_table в проекті не використовується, але вона дозволяє перезаписати таблицю з БД з деякими початковими записами
    def init_table(self):
        db = sqlite.connect(self.database)
        with db:
            conn = db.cursor()
            conn.execute("DROP TABLE {}".format(self.table))
            # звідси видно, які поля має таблиця для збереження табелів працівників
            conn.execute("CREATE TABLE {} (id INTEGER, employeeId INTEGER, month INTEGER, year INTEGER, hours TEXT)".format(self.table))
            db.commit()

            tables = (
                (1, 1, 1, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (2, 1, 2, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (3, 1, 3, 2015, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (4, 1, 4, 2015, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (5, 1, 5, 2015, "8 v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (6, 1, 6, 2015, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (7, 1, 7, 2015, "v v 8 8 9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (8, 1, 8, 2015, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (9, 1, 9, 2015, "v v 8 8 8 8 10 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (10, 1, 10, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (11, 1, 11, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (12, 1, 12, 2016, "v v 8 8 8 8 8 5 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (13, 2, 1, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (14, 2, 2, 2016, "v v 8 8 8 8 8 8 4 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (15, 2, 3, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (16, 2, 4, 2016, "v v 8 8 8 8 8 8 8 8 8 2 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (17, 2, 5, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (18, 2, 6, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (19, 2, 7, 2016, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (20, 2, 8, 2016, "v v 8 8 8 8 8 8 8 8 8 8 1 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (21, 2, 9, 2015, "v v 8 8 8 8 8 8 8 8 8 8 h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (22, 2, 10, 2015, "v v 8 8 8 8 8 8 8 h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (23, 2, 11, 2015, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (24, 2, 12, 2015, "v v 8 8 8 8 8 8 6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (25, 3, 1, 2017, "v v 8 8 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (26, 3, 2, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (27, 3, 3, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 0 8 8 8 8 8 8 8 8 8 8 8 8"),
                (28, 3, 4, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1 8 8 8 8 8 8 8 8 8 8 8 8"),
                (29, 3, 5, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 7 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (30, 3, 6, 2017, "v v 8 8 8 8 8 8 8 8 8 6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (31, 3, 7, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (32, 3, 8, 2017, "v v 8 8 8 8 8 8 8 h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (33, 3, 9, 2016, "v v v v v v v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (34, 3, 10, 2016, "h h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (35, 3, 11, 2016, "h h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (36, 3, 12, 2016, "h h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (37, 4, 1, 2017, "v v 8 8 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (38, 4, 2, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (39, 4, 3, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 0 8 8 8 8 8 8 8 8 8 8 8 8"),
                (40, 4, 4, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1 8 8 8 8 8 8 8 8 8 8 8 8"),
                (41, 4, 5, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 7 8 8 3 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (42, 4, 6, 2017, "v v 8 8 8 8 8 8 8 8 8 6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (43, 4, 7, 2017, "v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (44, 4, 8, 2017, "v v 8 8 8 8 8 8 8 h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (45, 4, 9, 2016, "v v v v v v v v 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (46, 4, 10, 2016, "h h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (47, 4, 11, 2016, "h h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8"),
                (48, 4, 12, 2016, "h h 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8")
            )

            conn.executemany("INSERT INTO {} (id, employeeId, month, year, hours) VALUES (?, ?, ?, ?, ?)"
                             .format(self.table), tables)
            db.commit()

    def add_to_db(self, name, month, year, hours):
        try:
            db = sqlite.connect(self.database)
            with db:
                conn = db.cursor()
                id = 1
                try:
                    conn.execute("SELECT MAX(id) FROM {}".format(self.table))
                    db.commit()

                    max_id = conn.fetchall()
                    id = max_id[0][0] + 1
                except Exception as e:
                    print("Inserting into empty table: " + self.table + " new index equals " + str(id))

                employees = Employee().get_all_db_data()
                employeeId = 0
                for employee in employees:
                    if name == employee["name"]:
                        employeeId = employee["id"]

                new_table = (id, employeeId, month, year, hours)

                conn.execute(
                    "INSERT INTO {} (id, employeeId, month, year, hours) VALUES (?,?,?,?,?)"
                        .format(self.table), new_table
                )

        except Exception as e:
            print("Troubles with add_commodity_to_db: " + e.args[0])
