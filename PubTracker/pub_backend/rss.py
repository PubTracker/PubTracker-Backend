__author__ = 'gubrian'

import feedparser

## The function will parse all the items in the rss feed, and make them as list of dict
def rss_parse(title):
    python_wiki_rss_url = title
    feed = feedparser.parse( python_wiki_rss_url )
    items = feed[ "items" ]
    for item in items:
        print(item["title"])


rss_parse("http://jvi.asm.org/rss/current.xml")