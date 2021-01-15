from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row #db connection returns rows like a python dictionary
    return connection

@app.route('/')
def index():
    """ Retrieve the posts from the db connection and pass it as part of render """
    connection = get_db_connection()
    posts = connection.execute('SELECT * from posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

