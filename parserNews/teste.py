# -*- coding: utf-8 -*-
import nltk
import nltk.data
from nltk.corpus import stopwords


sentences = u"Hospital recebeu hoje dois equipamentos oferecidos pela Fundação EDP, ao abrigo de um programa que vai ajudar mais quatro unidades do SNS com serviço de pediatria."
sentence_sem_stop = []
vec = []
f = open("../trainingdata/chave.MF300.txt", 'r')
for line in f:
    line = line.strip()
    vec.append(line)



tokens = nltk.tokenize.word_tokenize(sentences, 'portuguese')
print tokens
for w in tokens:
    p = w.lower()
    if p not in vec:
        sentence_sem_stop.append(w)

print sentence_sem_stop
pos = nltk.pos_tag(sentence_sem_stop)
sentt = nltk.ne_chunk(pos)

# print sentt

person = []
person_list = []
name = ""
# for chunk in sentt:
#     if hasattr(chunk, 'label') and chunk.label():
#                     if chunk.label() == 'PERSON' or chunk.label() == 'ORGANIZATION':
#                         print "****", chunk.leaves()
#                         print chunk.label(), ' '.join(c[0] for c in chunk.leaves())


for t in sentt:
    print t
    if hasattr(t, 'label') and t.label:

        if t.label() == 'PERSON' or t.label() == 'ORGANIZATION':
            for leaf in t.leaves():
                person.append(leaf[0])
            #if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''

            person = []
print person_list

# for sent in nltk.sent_tokenize(sentences):
#             for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#                 #print chunk
#                 if hasattr(chunk, 'label') and chunk.label():
#                     if chunk.label() == 'PERSON' or chunk.label() == 'ORGANIZATION':
#                         print chunk.label(), ' '.join(c[0] for c in chunk.leaves())