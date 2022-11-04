from flask import session
import sqlite3

def is_valid(email, senha):
    con = sqlite3.connect('database/database.db')
    cur = con.cursor()
    cur.execute('SELECT email, password FROM users')
    data = cur.fetchall()
    for row in data:
        if row[0] == email and row[1] == senha:
            return True
    return False

def getLoginDetails():
    with sqlite3.connect('database/database.db') as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            username = ''
            #noOfItems = 0
        else:
            loggedIn = True
            cur.execute("SELECT username FROM users WHERE email = '" + session['email'] + "'")
            username = cur.fetchone()
            ##cur.execute("SELECT count(productId) FROM bets WHERE userId = " + str(userId))
            ##noOfBets = cur.fetchone()[0]
    conn.close()
    return (loggedIn, username, session['email'])

def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    return conn