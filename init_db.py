import sqlite3

connection = sqlite3.connect('database.db') #creates db if not exists

with open('schema.sql') as file:
    connection.executescript(file.read())

cur = connection.cursor() #create cursor object to execute sql commands

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()