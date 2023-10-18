# I personally do strongly recommend you use a virtualenv, because it makes it much, much easier to swap out versions of libraries and not affect other Python projects. Without a virtualenv, you just continue with installing the dependencies, and they'll end up in your system libraries collection.

from flask import Flask, render_template

app = Flask(__name__)



        




@app.route("/for-loop/")
def hello_world():
    planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]
    return render_template(
        "for_loop.html", planets = planets
    )



@app.route("/for-loop-conditional/")
def hello_world2():

    users = {
        "Bob": "Mac",
        "Yash": "Windows",
        "John": "Linux"
    }

    
    return render_template(
        "for_loop_conditional.html", users=users
    )


