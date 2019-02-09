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

def get_users(con):
    with con.cursor() as cursor:
        cursor.execute('select * from users')
        users = cursor.fetchall()
    return users

@app.route('/')
def hello_world():
    with con.cursor() as cursor:
        cursor.execute('select * from users')
        users = cursor.fetchall()
        cursor.execute('select * from things')
        things = cursor.fetchall()
    return jsonify({
        'users': users,
        'things': things
    })

@app.route('/users/new', methods=['POST', 'GET'])
def create_user():
    if request.method == 'GET':
        return render_template('user_form.html')
    elif request.method == 'POST':
        name = request.form['name']
        with con.cursor() as cursor:
            sql='INSERT INTO `users` (`name`) VALUES (%s)'
            cursor.execute(sql, (name,))
        con.commit()
        return 'Thx'

@app.route('/things/new', methods=['POST', 'GET'])
def create_thing():
    if request.method == 'GET':
        users = get_users(con)
        return render_template('thing_form.html', users=users)
    elif request.method == 'POST':
        thing_name = request.form['thing']
        vote = True if request.form['vote'] == "1" else False
        user_id = request.form['user-select']
        user_id = int(user_id)
        with con.cursor() as cursor:
            sql='INSERT INTO `things` (`thing`, `vote`, `user_id`) VALUES (%s, %s, %s)'
            cursor.execute(sql, (thing_name, vote, user_id))
        con.commit()
        return 'Thx'
