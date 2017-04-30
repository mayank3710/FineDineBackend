from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/register/', methods=["GET","POST","request","put"])
def login_page():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    un_try = request.args.get('uid')
    pw_try = request.args.get('pass')
    name_try=request.args.get('name')



    ex = 0
    try:
        c.execute("SELECT * FROM user_data where uid=?",(un_try,))
        # c.execute("SELECT * FROM user_data")
        rows=c.fetchall()
        for row in rows:
            print(row)
            ex=1
            break
        #if data is None:
        if ex == 0:
            c.execute("INSERT INTO user_data VALUES (?,?,?)",(un_try,pw_try,name_try))
            conn.commit()
            return 'ho gaya'
        else:
            return 'already hai tu'

        #return '1 cool'
    except Exception as e:
        return 'galat'#RaiseToast that entry exists.


@app.route('/login/', methods=["GET","POST"])
def login_page1():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')

    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'admin' and password == 'pass':
        return 'Logged in'
    else:
        return 'Invalid creds'

@app.route('/logintry/', methods=["GET","POST"])
def login_page2():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    user_try = request.args.get('user_try')
    pass_try=request.args.get('pass_try')
    ex = 0
    try:
        c.execute("SELECT * FROM user_data where uid=? AND pass=?",(user_try,pass_try))
        # c.execute("SELECT * FROM user_data")
        rows=c.fetchall()
        for row in rows:
            #if rows.pass==pass_try:
            ex=1
            break
        #if data is None:
        if ex == 0:
            return 'pehchaana nahi'
        else:
            return 'arre tu phir aa gaya!'

        #return '1 cool'

    except Exception as e:
        return 'Kuch gadbada hai'#RaiseToast that entry exists.
