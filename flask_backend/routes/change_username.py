from flask import Blueprint, request, session, redirect, url_for, jsonify
from flask_cors import cross_origin
from flask_backend.services.utils import is_valid, get_db_connection

change_username = Blueprint('change_username', __name__)
@change_username.route('/change_username', methods = ['GET', 'POST'])
@cross_origin()

def show_change_username():
    if request.method == 'POST':
        username = str(request.form['username'])
        email = request.form['email']
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("UPDATE users SET username = '" + username + "' WHERE email = '" + email + "'")
        db.commit()

        #return redirect('http://localhost:3000/')
        return username