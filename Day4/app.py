# I personally do strongly recommend you use a virtualenv, because it makes it much, much easier to swap out versions of libraries and not affect other Python projects. Without a virtualenv, you just continue with installing the dependencies, and they'll end up in your system libraries collection.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/expressions/")
def hello_world():
    #interpolation

    color = "brown"
    animal_one = "dog"
    animal_two = "lion"

    #addition and subtraction

    orange_amount = 50
    apple_amount = 50
    donate_amount = 50


    #string concatenation

    first_name = "John"
    last_name = "Smith"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template(
        "expressions.html", **kwargs
    )
        

