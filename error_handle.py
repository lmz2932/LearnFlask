from flask import Flask, render_template, abort, redirect, url_for
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)


@app.errorhandler(401)
def error_401(error):
    resp = make_response(render_template('401.html'), 401)
    resp.headers['added'] = 'value'
    return resp
