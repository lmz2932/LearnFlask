from flask import Flask, url_for

app = Flask(__name__)


@app.route('/get/static/<string:filename>')
def static_url(filename):
    return url_for('static', filename=filename)
