from flask import Blueprint, request, redirect
from models.bet import Bet
from services.utils import get_db_connection
from flask_cors import cross_origin

delete_bet = Blueprint('delete_bet', __name__)
@delete_bet.route('/delete_bet', methods = ['GET', 'POST'])
@cross_origin()

def show_delete_bet():

    if request.method == 'POST':
        id_game = request.form['id_game']
        email = request.form['email']
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM bets WHERE id_game = '" + id_game + "' AND email = '" + email + "'")
        db.commit()
        return ok