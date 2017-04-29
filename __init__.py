# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Position import *
from Table import *
from Employee import *

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
        return render_template("main.html", error="Exception has been caught: " + e.args[0])

@app.route('/employees/')
def employees():
    try:
        POSTS_DATA = Position().get_all_db_data()
        EMPLOYEES_DATA = Employee().get_all_db_data()
        return render_template("employees.html", EMPLOYEES_DATA=EMPLOYEES_DATA, POSTS_DATA=POSTS_DATA, error=None)
    except Exception as e:
        return render_template("employees.html", error="Exception has been caught: " + e.args[0])


@app.route('/posts/')
def posts():
    try:
        POSTS_DATA = Position().get_all_db_data()
        return render_template("positionts.html", POSTS_DATA=POSTS_DATA, error=None)
    except Exception as e:
        return render_template("positionts.html", error="Exception has been caught: " + e.args[0])


@app.route("/tables/")
def tables():
    try:
        TABLES_DATA = Table().get_all_db_data()
        RENDERED_TABLES_DATA = Employee().render(TABLES_DATA)

        return render_template("tables.html", TABLES_DATA=RENDERED_TABLES_DATA, error=None)
    except Exception as e:
        return render_template("tables.html", error="Exception has been caught: " + e.args[0])

@app.route("/salaries/")
def salaries():
    return render_template("salaries.html")


"""
    Даний метод демонструє нам, як можна оброблювати форми за допомогою request та методів передачі
    GET та POST
"""
@app.route("/handler/", methods=["POST", "GET"])
def adding_tables_handler():
    if request.method == "POST":
        name = request.form["employee_name"]
        month = request.form["month"]
        year = request.form["year"]
        hours = request.form["hours"]

        Table().add_to_db(name, month, year, hours)

    return redirect(url_for("new_table"))

@app.route("/employees-handler/", methods=["POST", "GET"])
def employees_handler():
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

@app.route("/posts-handler/", methods=["POST", "GET"])
def posts_handler():
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
            Position().change_position(id, name, salary)

    return redirect(url_for("posts"))

@app.route("/new-table/")
def new_table():
    try:
        EMPLOYEES_DATA = Employee().get_all_db_data()
        return render_template("new-table.html", EMPLOYEES_DATA = EMPLOYEES_DATA, error=None)
    except Exception as e:
        return render_template("new-table.html", error="Exception has been caught: " + e.args[0])


if __name__ == "__main__":
    app.run()
