from flask import Flask, request

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def return_result():
    info = 'You search for:<br />'
    for key in request.args.keys():
        info += '%s=%s<br />' % (key, request.args[key])
    return info
