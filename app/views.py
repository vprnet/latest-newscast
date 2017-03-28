from index import app
from flask import render_template, request
from query import create_title
from config import BASE_URL

newscast_title = create_title()

@app.route("/")
def index():
    page_url = BASE_URL + request.path

    return render_template("base.html",
        newscast_title=newscast_title,
        page_url=page_url)
