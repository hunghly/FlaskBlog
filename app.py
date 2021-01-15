#The flash() function stores flashed messages in the client’s browser session, which requires setting a secret key. 
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row #db connection returns rows like a python dictionary
    return connection

def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    connection.close()
    if (post == None):
        abort(404)
    return post

@app.route('/')
def index():
    """ Retrieve the posts from the db connection and pass it as part of render """
    connection = get_db_connection()
    posts = connection.execute('SELECT * from posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')



# @app.route('/getNoteText',methods=['GET','POST'])
# def GetNoteText():
#     if request.method == 'POST':
#         file = request.files['pic']
#         filename = file.filename
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         processImage(filename)
#     else:
#         return "Y U NO USE POST?"
