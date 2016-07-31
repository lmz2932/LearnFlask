from flask import Flask, render_template, request, make_response, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
file_dir = './uploaded/'


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
            resp = make_response(render_template('upload_file.html'))
            resp.set_cookie('username', request.form['username'])
            return resp
        else:
            return 'Invalid user!!'


@app.route('/upload', methods=['POST', 'GET'])
def get_file():
    if not request.cookies.get('username'):
        return jsonify({'result': 'failed', 'reason': 'Not logged in'})
    if request.method == 'GET':
        return render_template('upload_file.html')
    else:
        try:
            f = request.files.get('picture')
            f.save(file_dir + secure_filename(f.filename))
        except Exception, e:
            return jsonify({'result': 'failed', 'reason': str(e)})
        else:
            return jsonify({'result': 'success'})
