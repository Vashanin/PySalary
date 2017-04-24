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
    return render_template("posts.html")

@app.route("/tables/")
def tables():
    return render_template("tables.html")

@app.route("/salaries/")
def salaries():
    return render_template("salaries.html")

@app.route("/new-table/")
def new_table():
    return("Here must be adding form")

if __name__ == "__main__":
    app.run()
