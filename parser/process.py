from whoosh.index import create_in
from whoosh.fields import *
from whoosh.index import open_dir
from whoosh.qparser import *

def indexer(data):

    schema = Schema(link=TEXT(stored=True), title=TEXT(stored=True), summary=TEXT(stored=True), content=TEXT(stored=True))
    ix = create_in("pulledfeeds", schema)

    writer = ix.writer()

    for item in data:
        writer.add_document(link=item['link'],
                            title=item['title'],
                            summary=item['summary'],
                            content=item['content'])

    writer.commit()

def query_index(query, index, maxlimit):
    ix = open_dir(index)

    query_results = []

    with ix.searcher() as searcher:
        query = MultifieldParser(["content", "summary", "title"], schema=ix.schema, group=OrGroup).parse(query)
        results = searcher.search(query, limit=100, terms=True)

        for hit in results:
            query_results.append({
                'link': hit['link'],
                'title': hit['title'],
                'highlights': hit.highlights("content"),
                'summary': hit['summary']
            })

    return query_results
