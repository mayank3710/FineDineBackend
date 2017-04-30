from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/reviews/write', methods=["GET","POST","request","put"])
def review_write():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    rest_try = request.args.get('rid')
    user_try=request.args.get('uid')
    rating_try=request.args.get('rating')
    review_try=request.args.get('review')
    date_try=request.args.get('date')
    c.execute('''DROP TABLE if exists review_rating ''')
    c.execute('''CREATE TABLE review_rating(rest_id int, uid INTEGER, rating int, review text, date text)''')
    c.execute("INSERT INTO review_rating VALUES (1,1,3,'This is a text reivew.','24/04/17')")
    conn.commit()
    return 'sucessfully reset review table'

@app.route('/review/show_review', methods=["GET","POST","request","put"])
def review_show():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    rest_try=request.args.get('rest_id')
    c.execute("SELECT * FROM food_menu where rid=?",(rest_try))
    rows=c.fetchall()
    for row in rows:
        print(row)
