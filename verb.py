# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return 'Method POST'
    else:
        return 'Method GET'
