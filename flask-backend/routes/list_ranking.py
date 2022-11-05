from flask import Blueprint, jsonify
from services.utils import get_db_connection

list_ranking = Blueprint('list_ranking', __name__)
@list_ranking.route('/list_ranking', methods = ['GET'])

def show_list_ranking():
    db = get_db_connection()
    cursor = db.cursor()
    query = "SELECT username, score, image FROM users WHERE email <> 'admin@admin.com' ORDER BY score desc"
    cursor.execute(query)
    users = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    
    return jsonify(users)