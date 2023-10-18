# I personally do strongly recommend you use a virtualenv, because it makes it much, much easier to swap out versions of libraries and not affect other Python projects. Without a virtualenv, you just continue with installing the dependencies, and they'll end up in your system libraries collection.

from flask import Flask, render_template

app = Flask(__name__)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third= third
        self.fourth = fourth
        




@app.route("/data-structures/")
def hello_world():
    movies = [
        "Bridge to Terabitthia",
        "Ultimate Spider Man",
        "Robot 2.o"
    ]

    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020"
    }

    moons = GalileanMoons("Io", "Europa", "Callisto", "Ganymede")

    kwargs = {
        "movies":  movies,
        "car": car,
        "moons": moons,


    }
    
    # return render_template(
    #     "data_structures.html", movies=movies, car=car, moons=moons
    # )
    return render_template(
        "data_structures.html", **kwargs
    )


        

