# The design and project idea is not mine 
# Credits to - udemy.com/user/josesalvatierra
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    entries_with_date = []  # Define it here, so it's accessible in all cases.

    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
        print(entry_content, formatted_date)
        entries.append((entry_content, formatted_date))

    # Move this outside the if block.
    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1],  "%d-%m-%Y").strftime("%b %d")
        )
        for entry in entries
    ]

    return render_template(
        "index.html", entries=entries_with_date
    )
