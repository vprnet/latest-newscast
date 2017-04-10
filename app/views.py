from index import app
from flask import render_template, request
from query import get_timestamp
from config import BASE_URL

newscast_title = get_timestamp()

@app.route("/")
def index():
    page_url = BASE_URL + request.path

    return render_template("base.html",
        newscast_title=newscast_title,
        page_url=page_url)
