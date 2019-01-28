from flask import Flask, render_template, request, jsonify
import yaml
import pymysql.cursors

app = Flask(__name__)

def unlock():
     with open("secret.yml", 'r') as stream:
         return yaml.load(stream)

# MySQL configurations
config = unlock()

con = pymysql.connect(
    host=config['dbhost'],
    user=config['user'],
    password=config['password'],
    db=config['dbname'],
    cursorclass=pymysql.cursors.DictCursor
)

def connect():
    config = unlock()
    app.config

@app.route('/')
def hello_world():
    with con.cursor() as cursor:
        cursor.execute('select * from users')
        result = cursor.fetchall()
    return jsonify(result)

@app.route('/users/new', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        name = request.form['name']
        with con.cursor() as cursor:
            sql='INSERT INTO users (name) VALUES (%s)'
            cursor.execute(sql, (name,))
        con.commit()
        return 'Thx'
