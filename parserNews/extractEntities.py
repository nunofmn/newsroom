import sqlite3 as lite

def save_entities(url, lista_referencias):
    con = lite.connect('test.db')

    with con:

        cur = con.cursor()
        cur.execute("create table if not exists Referencias (Url TEXT, Entidades TEXT)")
        #cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Referencias (Url, Entidades) VALUES(?,?)",(url, lista_referencias))

        # f = open("trainingdata/persons.txt", 'r')
        # grafo = {}
        # for line in f:
        #     line = line.rstrip()
        #     line = line.replace("http://pt.wikipedia.org/wiki/", "")
        #     line = line.replace("_", " ")
        #     cur.execute("INSERT INTO Persons VALUES("+ line +",'mmmm')")
    con.commit()
    print "Records created successfully";
    con.close()

def get_entities(url):
    con = lite.connect('test.db')
    result = ""
    with con:

        cursor = con.execute("SELECT Entidades from Referencias WHERE Url=?", (url,))
        con.commit()
        for row in cursor:
            result = row[0]


    con.close()
    return result