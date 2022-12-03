from flask import Blueprint, redirect
import sqlite3
from flask_backend import dbFilePath

delete_account = Blueprint('delete_account', __name__)
@delete_account.route("/delete_account")

def show_delete_account():
    con = sqlite3.connect(dbFilePath)
    cur = con.cursor()
    cur.execute("SELECT email FROM users WHERE logged = 1")
    email = cur.fetchone()
    email2 = ' '.join([str(elem) for elem in email])
    cur.execute("DELETE FROM bets WHERE email = '" + email2 + "'") 
    cur.execute("DELETE FROM users WHERE logged = 1")
    con.commit()
    return redirect('http://localhost:3000/signin')