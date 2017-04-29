# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

# в даному проекті користуємося SQLite

class Employee:
    """
        Даний клас виконує всі необхідні дії, що пов'язані з Працівниками: додавання/видалення/зчитування
        з бази данних.
        Функція render з масиву tuple, що було зчитано з бази даних Table формує асоціативний масив, який
        потім буде виводитися в файлі new-table.html
    """
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

    def render(self, request):
        EMPLOYEES_DATA = self.get_all_db_data()
        employee_dict = {}
        posts_dist = {}
        month_dict = {
            1 : "January",
            2 : "February",
            3 : "March",
            4 : "April",
            5 : "May",
            6 : "June",
            7 : "July",
            8 : "August",
            9 : "September",
            10: "October",
            11: "November",
            12: "December"
        }

        for item in EMPLOYEES_DATA:
            id = item[0]
            name = item[1]
            post = item[2]
            employee_dict[id] = name
            posts_dist[id] = post

        response = {}
        for item in request:
            year = item["year"]
            month = month_dict[item["month"]]
            response[year] = {}

        for item in request:
            year = item["year"]
            month = month_dict[item["month"]]
            response[year][month] = []

        for item in request:
            id = item["id"]
            employeeId = item["employeeId"]
            year = item["year"]
            month = month_dict[item["month"]]
            hours = item["hours"]

            employee = {
                "id" : id,
                "name" : employee_dict[employeeId],
                "post" : posts_dist[employeeId],
                "hours" : hours
            }

            response[year][month].append(employee)

        return response

    def add_new_employee(self, name, post, rate):
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

                employee = (id, name, post, rate)

                conn.execute(
                    "INSERT INTO {} (id, name, post, rate) VALUES (?,?,?,?)".format(self.table), employee
                )

        except Exception as e:
            print("Troubles with add_commodity_to_db: " + e.args[0])


    def remove_employee(self, id):
        try:
            db = sqlite.connect(self.database)
            with db:
                conn = db.cursor()
                conn.execute("DELETE FROM {} WHERE id={}".format(self.table, id))
        except Exception as e:
            print(e.args)

    def change_employee(self, id, name, post, rate):
        try:
            db = sqlite.connect(self.database)
            with db:
                conn = db.cursor()

                print(id)
                print(name)
                print(post)
                print(rate)

                conn.execute("SELECT * FROM {} WHERE id={}".format(self.table, id))

                responce = conn.fetchall()
                print(responce)

                if (len(name) == 0):
                    name = "{}".format(responce[0][1])

                if (len(post) == 0):
                    post = "{}".format(responce[0][2])

                if (len(rate) == 0):
                    rate = "{}".format(responce[0][3])
    
                conn.execute(
                    "UPDATE {} SET name = '{}', post = '{}', rate = '{}' WHERE id = "
                        .format(self.table, name, post, rate, id)
                )
        except Exception as e:
            print("Troubles with change_employee: " + e.args[0])


    # функція init_table в проекті не використовується, але вона дозволяє перезаписати таблицю з БД з деякими початковими записами
    def init_table(self):
        db = sqlite.connect(self.database)
        db.row_factory = sqlite.Row

        with db:
            conn = db.cursor()
            employees = (
                (1, "John Smith", "HR", 120),
                (2, "Isaac Jackson", "Team Lead", 150),
                (3, "Garry Hart", "Software Tester", 135),
                (4, "Colin Sparks", "Middle Python Developer", 190),
                (5, "Dorothy Hampton", "Data Scientist", 120),
                (6, "Mitchell Poole", "Team Lead", 150),
                (7, "Chloe Scott", "Software Tester", 135),
                (8, "Mae Lawson", "HR", 190),

            )
            conn.execute("DROP TABLE {}".format(self.table))
            db.commit()

            """
                Як видно звідси, таблиця для збереження інформції про працівників складається з трьох
                полів - ідентифікатор, ПІБ, посада та к-ть годин, що необхідно відробити за місяць
            """

            conn.execute("CREATE TABLE {} (id INTEGER, name TEXT, post TEXT, rate INTEGER)".format(self.table))
            db.commit()

            conn.executemany("INSERT INTO {} (id, name, post, rate) VALUES (?, ?, ?, ?)".format(self.table), employees)
            db.commit()