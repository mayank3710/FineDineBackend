from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register/users/merchant', methods=["GET","POST","request","put"])
def register_user_merchant():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    un_try = request.args.get('o_em')
    pw_try=request.args.get('o_pass')
    name_try=request.args.get('o_name')
    ex = 0
    try:
        c.execute("SELECT * FROM user_merchant_data where owner_email=?",(un_try,))
        # c.execute("SELECT * FROM user_data")
        rows=c.fetchall()
        for row in rows:
            print(row)
            ex=1
            break
        #if data is None:
        if ex == 0:
            c.execute("INSERT INTO user_merchant_data VALUES (?,?,?,?)",(null,un_try,pw_try,name_try))
            conn.commit()
            return 'ho gaya merchant'
        else:
            return 'already hai tu merchant'

        #return '1 cool'
    except Exception as e:
        return 'galat merchant'#RaiseToast that entry exists.


@app.route('/login1/', methods=["GET","POST","request","put"])
def login_user_merchant():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    email_try = request.args.get('email_try')
    pass_try=request.args.get('pass_try')
    ex = 0
    try:
        c.execute("SELECT * FROM user_merchant_data where owner_email=? AND pass=?",(email_try,pass_try))
        # c.execute("SELECT * FROM user_data")
        rows=c.fetchall()
        for row in rows:
            #if rows.pass==pass_try:
            ex=1
            break
        #if data is None:
        if ex == 0:
            return 'galat jawab'
        else:
            return 'sahi id pass hai'

        #return '1 cool'

    except Exception as e:
        return 'galat merchant'#RaiseToast that entry exists.
