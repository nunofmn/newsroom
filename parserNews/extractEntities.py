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

