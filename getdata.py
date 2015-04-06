from parser import feed
from parser import process

feeds = ["http://feeds.dn.pt/DN-Portugal", "http://feeds.jn.pt/JN-Pais"]


for url in feeds:
    process.indexer(feed.import_feed(url))
