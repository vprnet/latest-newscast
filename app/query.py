#!/usr/bin/python
import feedparser

def get_timestamp():
    latest_newscast_feed = "https://podcasts.vpr.net/newscasts"
    parsed_feed = feedparser.parse(latest_newscast_feed)

    return parsed_feed["date"]

def create_title():
    
    return str("VPR Newscast: ") + get_timestamp()


# what it gives: Mon, 27 Mar 2017 16:20:36 GMT
# what i want: VPR Newscast: 03/27/17 12:20 p.m.
