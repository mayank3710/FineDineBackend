from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/orders/table', methods=["GET","POST","request","put"])
def ordertable_reset():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    c.execute('''DROP TABLE if exists order_table ''')
    c.execute('''CREATE TABLE order_table(uid int,rid int, tid text, time text, date text, food_order text, addn text)''')
    c.execute("INSERT INTO order_table VALUES (1,1,'t1_4','10.30PM','24/04/17','food item 1/nfood item 2','Additonal requirements testing.')")
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

@app.route('/menu/db', methods=["GET","POST","REQUEST","PUT"])
def menu_commitdb():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    c.execute('''DROP TABLE if exists food_menu ''')
    c.execute('''CREATE TABLE food_menu(item_id INTEGER PRIMARY KEY AUTOINCREMENT, rid INTEGER, f_name text, f_price INTEGER, f_cat text)''')
    c.execute("INSERT INTO food_menu VALUES (null,1,'Paneer Butter Masala', 150,'INDIAN')")
    conn.commit()
    return 'sucessfully reset food menu'

@app.route('/menu1', methods=["GET","POST","REQUEST","PUT"])
def menu_additem():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    rest_try=request.args.get('rest')
    name_try = request.args.get('name')
    price_try=request.args.get('price')
    cat_try=request.args.get('cat')
    ex = 0
    try:
        c.execute("SELECT * FROM food_menu where rid=? AND f_name=?",(rest_try,name_try))
        # c.execute("SELECT * FROM user_data")
        rows=c.fetchall()
        for row in rows:
            print(row)
            ex=1
            break
        #if data is None:
        if ex == 0:
            c.execute("INSERT INTO food_menu VALUES (?,?,?,?,?)",(null,rest_try,name_try,price_try,cat_try))
            conn.commit()
            return 'item registered'
        else:
            return 'Item Already exists.'

        #return '1 cool'
    except Exception as e:
        return 'Some exception.'#RaiseToast that entry exists.


@app.route('/menu/show_items/', methods=["GET","POST","request","put"])
def menu_showitems():

    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.cursor()
    rest_try=request.args.get('rest_id')
    c.execute("SELECT * FROM food_menu where rid=?",(rest_try))
    rows=c.fetchall()
    final_result = []
    for row in rows:
        final_result.append({"dish_name" : row[2]})
    print (final_result)
    c.close()
    conn.close()
    return jsonify(final_result)
