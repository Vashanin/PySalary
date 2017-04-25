# -*- coding: utf-8 -*

import sqlite3 as sqlite

class Post:

    """
        Клас Post створено для будь-якої взаємодій, що пов'язана з посадами: додання/видалення/редагування,
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
