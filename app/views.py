from index import app
from flask import render_template, request
from query import get_timestamp, get_latest_episode
from config import BASE_URL

newscast_title = get_timestamp()
newscast_audio = get_latest_episode()

@app.route("/")
def index():
    page_url = BASE_URL + request.path

    return render_template("base.html",
        newscast_title=newscast_title,
        newscast_audio=newscast_audio,
        page_url=page_url)
