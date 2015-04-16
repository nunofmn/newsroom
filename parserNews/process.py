from whoosh.index import create_in
import whoosh.index as index
from whoosh.fields import *
from whoosh.index import open_dir
from whoosh.qparser import *
import nltk
import nltk.data
import os, os.path
import extractEntities as save_ent
from whoosh.analysis import LanguageAnalyzer
#nltk.download('all')


person_list = []
person = []
name = ""

def indexer(data):
    ana = LanguageAnalyzer("pt")
    schema = Schema(link=TEXT(stored=True), title=TEXT(stored=True, analyzer=ana), summary=TEXT(stored=True, analyzer=ana), content=TEXT(stored=True, analyzer=ana))

    if not os.path.exists("pulledfeeds"):
        os.mkdir("pulledfeeds")
        ix = create_in("pulledfeeds", schema)
    else:
        ix = index.open_dir("pulledfeeds")
    writer = ix.writer()

    for item in data:
        if item['content'] == '':
            cont = u" "
        else:
            cont = item['content']
        writer.add_document(link=item['link'],
                            title=item['title'],
                            summary=item['summary'],
                            content=cont)
    writer.commit()


    for item in data:
        link=item['link']
        title=item['title']
        summary=item['summary']
        content=item['content']

        sentencesArray = [title, summary, content ]

        person_list = []
        for sentences in sentencesArray:

            #sentences = title + " " + summary + " " + content
            tokens = nltk.tokenize.word_tokenize(sentences, 'portuguese')
            pos = nltk.pos_tag(tokens)
            sentt = nltk.ne_chunk(pos, binary = False)

            # print sentt

            person = []
            name = ""
            for t in sentt:
                if hasattr(t, 'label') and t.label:
            #print t.label()
                    if t.label() == 'PERSON':
                        for leaf in t.leaves():
                            person.append(leaf[0])
                        if len(person) > 1: #avoid grabbing lone surnames
                            for part in person:
                                name += part + ' '
                            if name[:-1] not in person_list:
                                person_list.append(name[:-1])
                            name = ''
                        person = []
        entidades = "| "
        for ent in person_list:
            entidades += ent + " | "
        if len(person_list) == 0:
            entidades = " none"

        entidades2 = "| "
        for ent in person_list:
            if save_ent.checkIfEntityWikiExists(ent):
                entidades2 += ent + " | "
        save_ent.save_entities(link, entidades)
        print "entidades ", entidades
        print "entidades2 ", entidades2


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
                'summary': hit['summary'],
                'entities': save_ent.get_entities(hit['link'])
            })


    return query_results
