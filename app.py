from parser import process 

print("Newsroom search app")
print("To exit press 0")

while True:
    query = raw_input("Insert your query:\n")

    if(query == '0'):
        break

    data = process.query_index(query, "pulledfeeds", 100)
    print data
