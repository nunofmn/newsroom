# encoding=utf8
import sqlite3 as lite

def save_entities(url, lista_referencias):
    con = lite.connect('test.db')

    with con:

        cur = con.cursor()
        cur.execute("create table if not exists Referencias (Url TEXT, Entidades TEXT)")
        cur.execute("INSERT INTO Referencias (Url, Entidades) VALUES(?,?)",(url, lista_referencias))
    con.commit()
    print "Records created successfully";
    con.close()

def checkIfUrlAlreadyParsed(url):
    con = lite.connect('test.db')
    result = ""
    with con:
        cur = con.cursor()
        cur.execute("create table if not exists Referencias (Url TEXT, Entidades TEXT)")
        cursor = con.execute("SELECT Url from Referencias WHERE Url=?", (url,))
        con.commit()
        for row in cursor:
            result = row[0]


    con.close()
    return result != ""

def get_entities(url):
    con = lite.connect('test.db')
    result = ""
    with con:
        cur = con.cursor()
        cur.execute("create table if not exists Referencias (Url TEXT, Entidades TEXT)")
        cursor = con.execute("SELECT Entidades from Referencias WHERE Url=?", (url,))
        con.commit()
        for row in cursor:
            result = row[0]


    con.close()
    return result


def generateWikiEntities():
    con = lite.connect('test.db')

    with con:

        cur = con.cursor()
        cur.execute("create table if not exists Wiki (Nome TEXT)")
        cur.execute("SELECT * FROM Wiki")
        data=cur.fetchall()
        if len(data)==0:
            f = open("trainingdata/persons.txt", 'r')
            for line in f:
                line = line.rstrip()
                line = line.replace("http://pt.wikipedia.org/wiki/", "")
                line = line.replace("_", " ")
                line = unicode(line, "utf-8")
                cur.execute("INSERT INTO Wiki (Nome) VALUES(?)",(line,))
        # else:
        #     #teste
        #     con = lite.connect('test.db')
        #
        #     for row in data:
        #         print row


    con.commit()
    print "Records created successfully";
    con.close()

def checkIfEntityWikiExists(name):
    con = lite.connect('test.db')
    result = ""
    with con:
        cursor = con.execute("SELECT Nome from Wiki WHERE Nome like ?", ('%'+name+'%',))
        con.commit()
        for row in cursor:
            result = row[0]


    con.close()
    return result  != ""


def save_relations(lista_entidades_relacionadas):
    con = lite.connect('test.db')
    lista_valores_anteriores = []
    for chave in lista_entidades_relacionadas:
        lista_valores_anteriores.append(string_to_array(get_relations(chave)))
    #estrutura->nome:num_noticias_diferentes
    with con:

        cur = con.cursor()
        cur.execute("create table if not exists Relacoes (Nome TEXT, Entidades TEXT)")
        print "entrou"
        for chave in lista_entidades_relacionadas:
            lista_sem_referencia = list(lista_entidades_relacionadas)
            if chave in lista_sem_referencia:
                lista_sem_referencia.remove(chave) # remove ele proprio da lista

            dicionario = {}
            lista_entidades_ja_percorridas = []
            for entidade in lista_valores_anteriores[0]:
                if len(entidade) > 0:
                    print "*****",entidade
                    par = entidade.split(":")
                    k = par[0]
                    v = par[1]
                    dicionario[k] = int(v)

            for entidade_nova in lista_sem_referencia:
                if dicionario.has_key(entidade_nova):
                    if entidade_nova not in lista_entidades_ja_percorridas:
                        dicionario[entidade_nova] += 1 #incrementa o numero de noticias em que aparece ambas as entidades
                    #incrementar valor uma vez apenas por noticia
                else:
                    dicionario[entidade_nova] = 1
                lista_entidades_ja_percorridas.append(entidade_nova)

            Entidades = ""
            for k, v in dicionario.items():
                # Display key and value.
                #print(k, v)
                Entidades+= k + ":" + str(v) + ","

            #Entidades = ",".join(lista_sem_referencia + list(set(lista_valores_anteriores[0]) - set(lista_sem_referencia)))
            #Entidades.replace(",,", ",");
            print "Chave {0} --> {1}".format( chave.encode('utf-8'), Entidades.encode('utf-8'))
            del lista_valores_anteriores[0]
            if Entidades.endswith(","):
                Entidades = Entidades[:-1]
            #Entidades = ",".join(lista_sem_referencia )
            if len(Entidades) > 0:
                cur.execute("INSERT OR REPLACE INTO Relacoes (Nome, Entidades) VALUES(?,?)",(chave, Entidades))
    con.commit()
    print "Records created successfully";
    con.close()


def get_relations(nome):
    con = lite.connect('test.db')
    result = ""
    with con:
        cur = con.cursor()
        cur.execute("create table if not exists Relacoes (Nome TEXT, Entidades TEXT)")
        cursor = con.execute("SELECT Entidades from Relacoes WHERE Nome=?", (nome,))
        con.commit()
        for row in cursor:
            result = row[0]


    con.close()
    return result

def get_all_relations():
    con = lite.connect('test.db')
    final = ""
    with con:
        cur = con.cursor()
        cur.execute("create table if not exists Relacoes (Nome TEXT, Entidades TEXT)")
        cursor = con.execute("SELECT * from Relacoes ")
        con.commit()
        nodes = []
        tmp_relations = []
        dicionario = {}
        count = 0
        for row in cursor:
            nodes.append(row[0].encode('UTF8'))
            tmp_relations.append(row[1].encode('UTF8'))
            print "**",row[0].encode('UTF8')
            print "--*",row[1].encode('UTF8')
            dicionario[row[0].encode('UTF8')] = count
            count +=1

        [x.encode('utf-8') for x in tmp_relations]
        link ='"links":['

        node_string = '{"nodes":['
        for node in nodes:
            node_string += '{"name":"'+ node +'"},'
        if node_string.endswith(","):
            node_string = node_string[:-1]
        node_string+='],'


        for relations in tmp_relations:
            rel = relations.split(",")
            myindex = tmp_relations.index(relations)
            for relation in rel:

                par = relation.split(":")
                nome = par[0].encode("utf-8") #nome
                print "---", nome
                v = par[1] #num vezes
                if dicionario[nome] > myindex:
                    link +='{"source":'+str(myindex)
                    link+= ',"target":'+ str(dicionario[nome]) + ',"value":'+ v + '},'
            print "++",row

        if link.endswith(","):
            link = link[:-1]
        link+= ']}'

        final = node_string+link
        final = final.encode("utf-8")
        print final


    con.close()
    return final

def string_to_array(frase):
    return  frase.split(',')

