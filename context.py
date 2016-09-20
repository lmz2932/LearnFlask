from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    return 'Successful!'

with app.test_request_context('/login', method='POST'):
    print request.method
    print request.path
    print dir(request)
