import os
from time import time
from flask import Flask, request,jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.environ['MONGOURL'])
app = Flask(__name__)
app.config['SECRET'] = os.environ['SECRET']
@app.route('/')
def hello_world():
    return jsonify({"message":f'Aishwary {time()}'}),200

if __name__ == '__main__':
    app.run(port=4000,debug=True if os.environ['ENV']=="DEV" else False)


