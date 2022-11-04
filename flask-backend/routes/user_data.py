from flask import Blueprint, session, jsonify
from services.utils import get_db_connection

user_data = Blueprint('user_data', __name__)
@user_data.route('/user_data', methods = ['GET'])

def show_user_data():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT email, username FROM users WHERE logged = 1")
    email, username = cursor.fetchone()
    data = [{'username': username, 'email': email}]
    return jsonify(data)