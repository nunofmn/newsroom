from parserNews import feed
from parserNews import process
from parserNews import extractEntities

feeds = ["http://feeds.dn.pt/DN-Portugal", "http://feeds.jn.pt/JN-Pais"]

#generates a table with all the wiki named entities
extractEntities.generateWikiEntities()

for url in feeds:
    process.indexer(feed.import_feed(url))
