from flask import session
import sqlite3, random

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

def getImage():
    images = [
        'https://images.unsplash.com/photo-1495360010541-f48722b34f7d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8Y2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Y2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1513245543132-31f507417b26?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDB8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1606225457115-9b0de873c5db?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDV8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60'
        'https://images.unsplash.com/photo-1592194996308-7b43878e84a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y2F0c3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1596854273338-cbf078ec7071?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDl8fGNhdHN8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1594367031514-3aee0295ec98?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTI0fHxjYXRzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1547045662-e5a75e7238c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTQ2fHxjYXRzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1572171572779-e93ec53b8024?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjMwfHxjYXRzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1579545255200-98c45be28788?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjcwfHxjYXRzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1607544155801-4f5af2e88dc6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjc0fHxjYXRzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
        'https://images.unsplash.com/photo-1548178235-bd0e8c71cc05?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzI2fHxjYXRzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
    ]

    return random.choice(images)