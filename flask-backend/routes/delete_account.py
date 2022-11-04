from flask import Blueprint, session, redirect
from services.utils import getLoginDetails
from routes.logout import show_logout
import sqlite3

delete_account = Blueprint('delete_account', __name__)
@delete_account.route("/delete_account")

def show_delete_account():
    if 'email' not in session:
        return 'user not in session'
    con = sqlite3.connect('database/database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE email = '" + session['email'] + "'")
    con.commit()
    return redirect('http://localhost:3000/signin')