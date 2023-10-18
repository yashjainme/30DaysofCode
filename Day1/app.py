# I personally do strongly recommend you use a virtualenv, because it makes it much, much easier to swap out versions of libraries and not affect other Python projects. Without a virtualenv, you just continue with installing the dependencies, and they'll end up in your system libraries collection.

from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello, world"
@app.route("/fancy")
def hello_world_fancy():
    return """
    <html>
    <body>

    <h1>Greetings</h1>
    <p>Hello, world</p>

    </body></html>

"""
