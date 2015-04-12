from parserNews import feed
from parserNews import process

feeds = ["http://feeds.dn.pt/DN-Portugal"]


for url in feeds:
    process.indexer(feed.import_feed(url))
