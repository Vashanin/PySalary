from Post import *

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/employees/')
def employees():
    return render_template("employees.html")

@app.route('/posts/')
def posts():
    POSTS_DATA = []
    try:
        post = Post()
        POSTS_DATA = post.get_all_db_data()
    except Exception as e:
        print("Exception inside posts(): " + e.args[0])

    return render_template("posts.html", POSTS_DATA = POSTS_DATA)

@app.route("/tables/")
def tables():
    return render_template("tables.html")

@app.route("/salaries/")
def salaries():
    return render_template("salaries.html")

@app.route("/new-table/")
def new_table():
    return render_template("new-table.html")

if __name__ == "__main__":
    app.run()
