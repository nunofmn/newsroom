from flask import Flask, jsonify, request, render_template
from parserNews import process
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/entities")
def entities():
    return render_template('entities.html')

@app.route("/entities/data")
def entitiesdata():
    return jsonify(
        {
          "nodes":[
              {"name":"Pedro Passos-Coelho"},
              {"name":"Paulo Portas"},
              {"name":"Estradas de Portugal"},
              {"name":"EDP"}
            ],
          "links":[
              {"source":0,"target":1,"value":5},
              {"source":0,"target":3,"value":2},
              {"source":1,"target":3,"value":2},
              {"source":1,"target":2,"value":1},
              {"source":2,"target":2,"value":4}
            ]
        }
    );

@app.route("/search", methods=['POST'])
def search():

    data = process.query_index(request.form['query'], "pulledfeeds", 100)
    print data
    return jsonify(results=data)

if __name__ == "__main__":
    app.run(debug=True)
