# I personally do strongly recommend you use a virtualenv, because it makes it much, much easier to swap out versions of libraries and not affect other Python projects. Without a virtualenv, you just continue with installing the dependencies, and they'll end up in your system libraries collection.

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('first_page.html')
@app.route("/second")
def hello_world_second():
    return render_template('second_page.html')
