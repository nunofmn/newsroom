from flask import Flask, jsonify, request
from parser import process
app = Flask(__name__)

@app.route("/")
def hello():
    return "Newsroom"

@app.route("/search", methods=['POST'])
def search():
    if not request.form['query']:
        abort(400)

    data = process.query_index(request.form['query'], "pulledfeeds", 100)
    print data
    return jsonify(results=data)

if __name__ == "__main__":
    app.run(debug=True)
