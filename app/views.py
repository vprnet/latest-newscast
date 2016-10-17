from index import app
from flask import render_template, request
from query import get_timestamp
from config import BASE_URL

results = get_timestamp()
test = str(results)
timestamp = test[:19] + test[22:]

@app.route("/")
def index():
    page_url = BASE_URL + request.path

    return render_template("base.html",
        timestamp=timestamp,
        page_url=page_url)
