from flask import Flask, render_template, request

app = Flask(__name__)


def valid_user(username, password):
    return username == 'test' and password == 'test'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if valid_user(
            request.form['username'],
            request.form['password']
        ):
            return 'Welcome!'
        else:
            return 'Invalid user!!'
