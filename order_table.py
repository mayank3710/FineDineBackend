from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/orders/table', methods=["GET","POST","request","put"])
def ordertable_reset():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    c.execute('''DROP TABLE if exists order_table ''')
    c.execute('''CREATE TABLE order_table(uid int,rid int, tid int, time text, date text, food_order text, addn text)''')
    c.execute("INSERT INTO order_table VALUES (1,1,1,'10.30PM','24/04/17','food item 1/nfood item 2','Additonal requirements testing.')")
    conn.commit()
    return 'sucessfully reset table orders.'

@app.route('/orders/book', methods=["GET","POST","request","put"])
def ordertable_book():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    uid_try=request.args.get('uid')
    rid_try=request.args.get('rid')
    tid_try=request.args.get('tid')
    time_try=request.args.get('time')
    date_try=request.args.get('date')
    food_try=request.args.get('food')
    addn_try=request.args.get('addn')
    c.execute("INSERT INTO order_table VALUES (?,?,?,?,?)",(uid_try,rid_try,tid_try,time_try,date_try,food_try,addn_try))

@app.route('/orders/history', methods=["GET","POST","request","put"])
def ordertable_history():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    uid_try=request.args.get('uid')
    rid_try=request.args.get('rid')
    tid_try=request.args.get('tid')
    time_try=request.args.get('time')
    c.execute("SELECT * FROM order_table where uid=? AND rid=? AND tid=? AND time=?",(uid_try,rid_try,tid_try,time_try))
    rows=c.fetchall()
    for row in rows:
        print(row)
