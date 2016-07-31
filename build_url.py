# -*- coding: utf-8 -*-
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    pass


@app.route('/login')
def login():
    pass


@app.route('/user/<username>')
def profile(userneme):
    pass

with app.test_request_context():
    # url_for会自动处理特殊字符转义，在模板中应用也很方便
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='marsloo')
