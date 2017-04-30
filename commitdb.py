from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/commitdb')
def commitall():
    import sqlite3
    conn = sqlite3.connect('fineDine.db')
    c=conn.commit()
    conn.close()
    return 'all committed'
