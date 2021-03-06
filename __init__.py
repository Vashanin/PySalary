# !/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from Position import *
from Table import *
from Employee import *
from Salary import *

from flask import Flask, render_template, flash, request, url_for, redirect

"""
    __init__.py - перший файл, який запускається в даному проекті. Тут створюється об'єкт app класу Flask
    та запускається на виконання
    
    Далі ми прив'язуємо функції, напр homepage та певну URL адресу, за яку вона буде відповідати.
    Наприклад, якщо в адресному рядку ми введемо 127.0.0.1:5000/tables/ - запуститься функція tables,
    а потім перенаправить нас на сторінку tables.html

    За допомогою функції render_template ми визначаємо на яку сторінку буде перенаправлено з даної функції,
    а також перелік інших аргументів, які будуть передані.
    Наприклад, можемо передати перний словник з набором значень, які потім будуть відображатися в браузері
    документі (див. коментарі до header.html)
"""


app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        return render_template("main.html", error=None)
    except Exception as e:
        traceback.format_exc()
        return render_template("main.html", error="Exception has been caught: " + e.args[0])

@app.route('/employees/')
def employees():
    try:
        POSTS_DATA = Position().get_all_db_data()
        EMPLOYEES_DATA = Employee().get_all_db_data()
        return render_template("employees.html", EMPLOYEES_DATA=EMPLOYEES_DATA, POSTS_DATA=POSTS_DATA, error=None)
    except Exception as e:
        traceback.format_exc()
        return render_template("employees.html", error="Exception has been caught: " + e.args[0])

@app.route('/positions/')
def positions():
    try:
        POSTS_DATA = Position().get_all_db_data()
        return render_template("positionts.html", POSTS_DATA=POSTS_DATA, error=None)
    except Exception as e:
        traceback.format_exc()
        return render_template("positionts.html", error="Exception has been caught: " + e.args[0])


@app.route("/tables/")
def tables():
    try:
        TABLES_DATA = Table().get_all_db_data()
        EMPLOYEES_DATA = Employee().get_all_db_data()

        indexes = []
        for item in TABLES_DATA:
            indexes.append(item[0])

        RENDERED_TABLES_DATA = Employee().render(TABLES_DATA)

        return render_template("tables.html", indexes=indexes, EMPLOYEES_DATA=EMPLOYEES_DATA, TABLES_DATA=RENDERED_TABLES_DATA, error=None)
    except Exception as e:
        return render_template("tables.html", indexes=[], TABLES_DATA={}, EMPLOYEES_DATA={}, error="Exception has been caught: " + e.args[0])


@app.route("/salaries/")
def salaries():
    try:
        SALARIES_INFO = Salary().calculate_salary_for_all()
        DATE_DICT = Salary().represent_as_date_dictionary(SALARIES_INFO)
        EMPLOYEE_DICT = Salary().represent_as_employee_dictionary(SALARIES_INFO)

        return render_template("salaries.html", error=None, DATE_DICT=DATE_DICT, EMPLOYEE_DICT=EMPLOYEE_DICT)
    except Exception as e:
        return render_template("salaries.html", error=("Exception has been caught: " + e.args[0]), DATE_DICT={}, EMPLOYEE_DICT={})

"""
    Даний метод демонструє нам, як можна оброблювати форми за допомогою request та методів передачі
    GET та POST
"""
@app.route("/handler/", methods=["POST", "GET"])
def adding_tables_handler():
    try:
        if request.method == "POST":
            name = request.form["employee_name"]
            month = request.form["month"]
            year = request.form["year"]
            hours = request.form["hours"]

            Table().add_to_db(name, month, year, hours)

        return redirect(url_for("new_table"))
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()

@app.route("/employees-handler/", methods=["POST", "GET"])
def employees_handler():
    try:
        if request.method == "POST":
            action = request.form["action"]
            id = request.form["id"]
            name = request.form["name"]
            post = request.form["post"]
            rate = request.form["rate"]

            if (action == "add"):
                Employee().add_new_employee(name, post, rate)
            if (action == "remove"):
                Employee().remove_employee(id)
            if (action == "edit"):
                Employee().change_employee(id, name, post, rate)

        return redirect(url_for("employees"))
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()

@app.route("/salaries-handler/", methods=["POST", "GET"])
def salaries_handler():
    return None

@app.route("/positions-handler/", methods=["POST", "GET"])
def posts_handler():
    try:
        if request.method == "POST":
            action = request.form["action"]
            id = request.form["id"]
            name = request.form["name"]
            salary = request.form["salary"]

            if (action == "add"):
                Position().add_new_position(name, salary)
            if (action == "remove"):
                Position().remove_post(id)
            if (action == "edit"):
                Position().edit_position(id, name, salary)

        return redirect(url_for("positions"))
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()

@app.route("/tables-handler/", methods=["POST", "GET"])
def tables_handler():
    try:
        if request.method == "POST":
            action = request.form["action"]
            id = request.form["id"]
            employee_name = request.form["employee_name"]
            month = request.form["month"]
            hours = request.form["hours"]
            year = request.form["year"]

            if (action == "add"):
                Table().add_table(employee_name, month, year, hours)
            if (action == "remove"):
                Table().remove_table(id)
            if (action == "edit"):
                Table().edit_table(id, employee_name, month, year, hours)

        return redirect(url_for("tables"))
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()


@app.route("/new-table/")
def new_table():
    try:
        EMPLOYEES_DATA = Employee().get_all_db_data()
        return render_template("new-table.html", EMPLOYEES_DATA = EMPLOYEES_DATA, error=None)
    except Exception as e:
        traceback.format_exc()
        return render_template("new-table.html", error="Exception has been caught: " + e.args[0])

if __name__ == "__main__":
    app.run()
