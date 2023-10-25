# I personally do strongly recommend you use a virtualenv, because it makes it much, much easier to swap out versions of libraries and not affect other Python projects. Without a virtualenv, you just continue with installing the dependencies, and they'll end up in your system libraries collection.

from flask import Flask, render_template

app = Flask(__name__)



        
todos=[
    ('hello, world', False),
    ('Namaste, world', True)]



@app.route("/")
def hello_world():
  
    return render_template(
        "home.html", todos=todos
    )






@app.route("/<string:todo>")
def todo_item(todo:str):
    for text, completed in todos:
        if text == todo:
            completed_text = "[x]" if completed else "[]"
            title = f"{completed_text} - Todos"

            return render_template(
                "todo.html", text = text, completed = completed, title = title
            )
    else:
        return render_template(
            "not-found.html", text = todo, title = "Not Found"
        )
