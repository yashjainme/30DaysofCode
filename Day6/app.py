# I personally do strongly recommend you use a virtualenv, because it makes it much, much easier to swap out versions of libraries and not affect other Python projects. Without a virtualenv, you just continue with installing the dependencies, and they'll end up in your system libraries collection.

from flask import Flask, render_template

app = Flask(__name__)



        




@app.route("/conditionals/")
def hello_world():
    
    company = "Apple"
 
    return render_template(
        "conditionals.html", company = company
    )


        

