# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from parserNews import process
from parserNews import extractEntities as save_ent


print("Newsroom search app")
print("To exit press 0")

while True:
    query = raw_input("Insert your query:\n")

    if(query == '0'):
        break

    if query == '1':
        q = raw_input("Insert relation search:\n")
        v =  save_ent.get_relations(unicode(q))
        print v
    elif query == '2':
        q = raw_input("kkk")
        save_ent.get_all_relations()
    else:
        data = process.query_index(query, "pulledfeeds", 200)
        for entry in data:
            print entry['link']
