from Post import *
from Table import *
from Employee import *

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/employees/')
def employees():
    try:
        employee = Employee()
        EMPLOYEES_DATA = employee.get_all_db_data()
        return render_template("employees.html", EMPLOYEES_DATA=EMPLOYEES_DATA, error=None)
    except Exception as e:
        return render_template("employees.html", error="Exception has been caught: " + e.args[0])


@app.route('/posts/')
def posts():
    try:
        post = Post()
        POSTS_DATA = post.get_all_db_data()
        return render_template("posts.html", POSTS_DATA=POSTS_DATA, error=None)
    except Exception as e:
        return render_template("posts.html", error="Exception has been caught: " + e.args[0])


@app.route("/tables/")
def tables():
    try:
        table = Table()
        TABLES_DATA = table.get_all_db_data()
        return render_template("tables.html", TABLES_DATA=TABLES_DATA, error=None)
    except Exception as e:
        return render_template("tables.html", error="Exception has been caught: " + e.args[0])

@app.route("/salaries/")
def salaries():
    return render_template("salaries.html")

@app.route("/new-table/")
def new_table():
    return render_template("new-table.html")

if __name__ == "__main__":
    app.run()
