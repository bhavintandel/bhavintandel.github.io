from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open("../index.html") as page:
        index = page.read()
    return index

@app.route('/aboutme')
def about_me():
    return "In Progress"

@app.route('/projects/')
def projects():
    return "In Progress"

@app.route('/projects/<string:project_name>')
def show_project(project_name):
    return "Project %s" %project_name + " is In Progress"

