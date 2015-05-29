__author__ = 'gubrian'

import feedparser
from models import RssNewsItem

## The function will parse all the items in the rss feed, and make them as list of dict
def rss_parse(url):
    python_wiki_rss_url = url
    feed = feedparser.parse(python_wiki_rss_url)
    items = feed["items"]
    result = []
    for item in items:
        rss_item = {}
        rss_item["title"] = item["title"]
        rss_item["summary"] = item["summary"]
        result.append(rss_item)
    return result
