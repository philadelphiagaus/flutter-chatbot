from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)


@app.route("/api", methods=['GET'])
def hello_world():
    
    d = {}      
    d['Query'] = str(request.args['Query'])
    return jsonify(d)
   
if __name__ == '__main__':
    app.run()