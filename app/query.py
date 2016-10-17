#!/usr/bin/python

import eyed3
import urllib

def get_timestamp():
    audiofile, headers = urllib.urlretrieve("http://www.vpr.net/mobile/vprnewscast.mp3")
    source = eyed3.load(audiofile)
    return source.tag.title
