from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/reset/users/client', methods=["GET","POST"])
def reset_database_usr_client():
    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    c.execute('''DROP TABLE if exists user_data
             ''')
    c.execute('''CREATE TABLE user_data
             (uid text, pass text, name text, PRIMARY KEY (uid))''')
    c.execute("INSERT INTO user_data VALUES ('mayank@gmail.com','mayank@123','Mayank Jain')")
    conn.commit()
    return 'sucessfully reset'

@app.route('/reset/users/merchant', methods=["GET","POST"])
def reset_database_user_merchant():
    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    c.execute('''DROP TABLE if exists user_merchant_data
             ''')
    c.execute('''CREATE TABLE user_merchant_data
             (own_id INTEGER PRIMARY KEY AUTOINCREMENT, owner_email text, pass text, name text)''')
    c.execute("INSERT INTO user_merchant_data VALUES (null,'mayank@gmail.com','mayank@123','Mayank Jain')")
    conn.commit()
    return 'sucessfully reset merchant table'

@app.route('/reset/restaurant', methods=["GET","POST"])
def reset_database_rest_data():
    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    c.execute('''DROP TABLE if exists rest_data
             ''')
    c.execute('''CREATE TABLE rest_data
             (rid INTEGER, rname text, own_id int, lat real, long real, phone text, email text, PRIMARY KEY (rid))''')
    c.execute("INSERT INTO rest_data VALUES (1,'Madhuvan Serai',2, 10.12345,32.12345,'+91 2101122','mayankjain@gmail.com')")
    conn.commit()
    return 'sucessfully done'
