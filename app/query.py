#!/usr/bin/python
import feedparser

def get_timestamp():
    latest_newscast_feed = "https://podcasts.vpr.net/newscasts"
    parsed_feed = feedparser.parse(latest_newscast_feed)
    parsed_title = parsed_feed["items"][0]["title"]
    
    return parsed_title


def get_latest_episode():
    latest_newscast_feed = "https://podcasts.vpr.net/newscasts"
    parsed_feed = feedparser.parse(latest_newscast_feed)
    parsed_audio = parsed_feed["items"][0]["enclosures"]

    return parsed_audio[0]["href"]
