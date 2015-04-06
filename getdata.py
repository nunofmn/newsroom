from parser import feed

feeds = ["http://feeds.jn.pt/JN-ULTIMAS", "http://feeds.dn.pt/DN-Ultimas"]

for url in feeds:
    feed.import_feed(url)
