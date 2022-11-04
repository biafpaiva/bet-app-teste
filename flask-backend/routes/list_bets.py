from flask import Blueprint, jsonify, session
from services.utils import get_db_connection, getLoginDetails
from flask_cors import cross_origin

list_bets = Blueprint('list_bets', __name__)
@list_bets.route('/list_bets', methods = ['GET'])
@cross_origin()

def show_list_bets():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT email FROM users WHERE logged = 1")
    email = cursor.fetchone()
    email2 = ' '.join([str(elem) for elem in email]) 
    query = "SELECT bets.email, matches.teams, matches.round FROM bets INNER JOIN matches ON bets.id_game=matches.id_ WHERE bets.email = '" + email2 + "'"
    cursor.execute(query)
    bets = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    
    return jsonify(bets)