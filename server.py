from flask import Flask, jsonify, request, render_template
from parserNews import process
from parserNews import extractEntities
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/entities")
def entities():
    return render_template('entities.html')

@app.route("/entities/data")
def entitiesdata():
    return extractEntities.get_all_relations()

@app.route("/search", methods=['POST'])
def search():

    data = process.query_index(request.form['query'], "pulledfeeds", 100)
    print data
    return jsonify(results=data)

if __name__ == "__main__":
    app.run(debug=True)
