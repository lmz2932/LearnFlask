from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/templates/<filename>')
def return_template(filename):
    return render_template(filename)

@app.route('/check', methods=['POST'])
def check():
    print request.form.get('name')
    return ""
