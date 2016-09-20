from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # 对.html、.htm、xml、xhtml支持自动转义
    return render_template('hello.html', name=name)
