#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

os.environ.get('LEDGER_URL')

connection_string = os.environ.get('LEDGER_URL')

cluster = MongoClient(connection_string, server_api = ServerApi('1'))

db = cluster['SignatureID']  # Database ID
col = db.Signature      # Collection ID

@app.route("/get", methods=['GET'])
def get_sig():
    signatures = col.find()
    sig_list = []
    for item in signatures:
        sig_dict = {
            "_id": item['_id'],
            "event": item['Event'],
            "id": item['id'],
            "date":item['date'],
            "sig": item['sig'],
            "payload": item['payload']
        }
        sig_list.append(sig_dict)
    
    return jsonify(sig_list)

@app.route('/hello', methods=['GET'])
def query():
    response_data = {'message': 'Hello World'}
    return jsonify(response_data)

@app.route("/test", methods=['POST'])
def testAPI():
    col.insert_one({'test_digiprime': 'successful'})
    return "/test success"

@app.route("/add", methods=['POST']) # Fixa så att man kan skicka från form input
def startpy():
    event = request.json['event']
    id = request.json['id']
    ledger_dict = {
        "event": event,
        "id": id
    }
    col.insert_one(ledger_dict)
    return "/add success"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=105)