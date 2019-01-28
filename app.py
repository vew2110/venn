from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new', methods=['POST', 'GET'])
def form(name=None):
    if request.method == 'GET':
        return render_template('form.html', name=name)
    elif request.method == 'POST':
        return 'Thx'
