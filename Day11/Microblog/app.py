# The design and project idea is not mine 
# Credits to - udemy.com/user/josesalvatierra

from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

app = Flask(__name__)

# Initialize the MongoClient with your connection string
client = MongoClient("Your_MongoDB_Atlas")
app.db = client.microblog
entries = []

@app.route("/", methods=["GET", "POST"])
def home():

    print([e for e in app.db.entries.find({})])
    entries_with_date = []  # Define it here, so it's accessible in all cases.

    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
        print(entry_content, formatted_date)
        entries.append((entry_content, formatted_date))
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})
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
