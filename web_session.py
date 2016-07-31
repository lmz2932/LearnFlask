from flask import Flask, render_template, request, session, escape, redirect
from flask import url_for

app = Flask(__name__)
app.secret_key = \
    '\xc2\xb3\x86U\x8fe\x1b0\x9b&\xae4\xa1]f\x83s\xf8\x7f\x13w\xc3'


def valid_user(username, password):
    return username == 'test' and password == 'test'


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    else:
        return 'You are not logged in!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if valid_user(
            request.form['username'],
            request.form['password']
        ):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return 'Invalid user!!'
