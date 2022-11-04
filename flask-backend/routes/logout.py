from flask import Blueprint, session, redirect, url_for
from services.utils import get_db_connection

logout = Blueprint('logout', __name__)
@logout.route('/logout', methods = ['GET'])

def show_logout():
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT email FROM users WHERE logged = 1")
    email = cur.fetchone()
    email2 = ' '.join([str(elem) for elem in email]) 
    cur.execute("UPDATE users SET logged = NULL WHERE email = '" + email2 + "'")
    db.commit()
    #session.pop('email', None)
    return redirect('http://localhost:3000/signin')
    #return email2