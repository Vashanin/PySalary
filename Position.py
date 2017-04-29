# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import traceback

class Position:

    """
        Клас Position створено для будь-якої взаємодій, що пов'язана з посадами: додання/видалення/редагування,
        що можна побачити з однойменних методів, які мають доступ до відповідних таблиць всередині баз даних,
        де зберігається вся інформація
    """

    def __init__(self, table="Posts", database="templates/db/database.db"):
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

    def add_new_position(self, name, salary):
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

                post = (id, name, salary)

                conn.execute(
                    "INSERT INTO {} (id, name, salaryPerHour) VALUES (?,?,?)".format(self.table), post
                )

        except Exception as e:
            print("Troubles with add_new_position: " + e.args[0])

    def remove_post(self, id):
        try:
            db = sqlite.connect(self.database)
            with db:
                conn = db.cursor()
                conn.execute("DELETE FROM {} WHERE id={}".format(self.table, id))
        except Exception as e:
            print(e.args)

    def change_position(self, id, name, salary):
        try:
            db = sqlite.connect(self.database)
            with db:
                conn = db.cursor()

                conn.execute("SELECT * FROM {} WHERE id={}".format(self.table, id))

                responce = conn.fetchall()

                if (len(name) == 0):
                    name = responce[0][1]

                if (len(salary) == 0):
                    salary = responce[0][2]

                conn.execute(
                    "UPDATE {} SET name = '{}', salaryPerHour = '{}' WHERE id = {}"
                        .format(self.table, name, salary, id)
                )
        except   Exception as e:
            print("Troubles with change_position: " + e.args[0])
            print(traceback.format_exc())