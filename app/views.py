from index import app
from flask import render_template, request
from query import get_timestamp
from config import BASE_URL

results = get_timestamp()
cleaned_time = str(results)
timestamp = cleaned_time[:19] + cleaned_time[22:]

@app.route("/")
def index():
    page_url = BASE_URL + request.path

    return render_template("base.html",
        timestamp=timestamp,
        page_url=page_url)
