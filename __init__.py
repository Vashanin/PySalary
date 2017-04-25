from Post import *
from Table import *
from Employee import *

from flask import Flask, render_template, flash, request, url_for, redirect

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
        EMPLOYEES_DATA = Employee().get_all_db_data()
        return render_template("employees.html", EMPLOYEES_DATA=EMPLOYEES_DATA, error=None)
    except Exception as e:
        return render_template("employees.html", error="Exception has been caught: " + e.args[0])


@app.route('/posts/')
def posts():
    try:
        POSTS_DATA = Post().get_all_db_data()
        return render_template("posts.html", POSTS_DATA=POSTS_DATA, error=None)
    except Exception as e:
        return render_template("posts.html", error="Exception has been caught: " + e.args[0])


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

@app.route("/new-table/", methods=["POST"])
def new_table():
    try:
        EMPLOYEES_DATA = Employee().get_all_db_data()
        return render_template("new-table.html", EMPLOYEES_DATA = EMPLOYEES_DATA, error=None)
    except Exception as e:
        return render_template("new-table.html", error="Exception has been caught: " + e.args[0])

if __name__ == "__main__":
    app.run()
