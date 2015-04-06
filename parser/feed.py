import feedparser
import requests
from bs4 import BeautifulSoup

def import_feed(url):
    parsed_data = []
    feed = feedparser.parse(url)

    for item in iter(feed['entries']):
        parsed_data.append({
            'title': item['title'],
            'link': item['link'],
            'summary': item['summary'].split("<img")[0],
            'content': article_parse(item['link'])
        })

    return parsed_data

def article_parse(url):
    article_text = ""
    print url

    html = BeautifulSoup(requests.get(url + "&page=-1").text)
    article = html.find(id='Article')

    if article:
        article = html.find(id='Article').find_all('p')

        for p in article:
            article_text = article_text + p.text + "\n"

        return article_text
    else:
        return unicode("")









