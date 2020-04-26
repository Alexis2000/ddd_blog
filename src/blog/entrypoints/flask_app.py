from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    return 'healthy', 200


@app.route("/add_post", methods=['POST'])
def add_batch():
    return 'OK', 201

