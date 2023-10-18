# The design and project idea is not mine 
# Credits to - udemy.com/user/josesalvatierra
from flask import Flask, render_template

app = Flask(__name__)



        




@app.route("/")
def home():
    
    return render_template(
        "index.html"
    )


