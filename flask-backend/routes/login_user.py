from flask import Blueprint, request, session, redirect, url_for
from flask_cors import cross_origin
from services.utils import is_valid, get_db_connection

login_user = Blueprint('login_user', __name__)

@login_user.route('/login_user', methods = ['GET', 'POST'])
@cross_origin()
def show_login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if is_valid(email, password):
            session['email'] = email
            
            db = get_db_connection()
            cur = db.cursor()
            cur.execute("UPDATE users SET logged = 1 WHERE email = '" + email + "'")
            db.commit()

            return redirect('http://localhost:3000/')
        else:
            error = 'Invalid UserId / Password'
            return error