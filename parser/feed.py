import feedparser

def import_feed(url):
    parsed_data = []
    feed = feedparser.parse(url)

    for item in iter(feed['entries']):
        parsed_data.append({
            'title': item['title'],
            'link': item['link'],
            'summary': item['summary'].split("<img")[0]
        })

    return parsed_data


