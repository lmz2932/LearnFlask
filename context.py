from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    return 'Successful!'

# with app.test_request_context('/login', method='POST'):
#     assert request.method == 'POST'
#     assert request.path == '/login'
