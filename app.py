from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/bot", method=["POST"])
@cross_origin()

# response
def response():
    query = dict(request.form)['query']
    result = query + " " + time.ctime()
    return jsonify({"response" : result})

if __name__ == "__main__" : 
       app.run(host="0.0.0.0", )