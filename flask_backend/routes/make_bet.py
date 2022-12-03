from flask import Blueprint, request, redirect
from flask_backend.models.bet import Bet
from flask_backend.services.utils import get_db_connection

make_bet = Blueprint('make_bet', __name__)
@make_bet.route('/make_bet', methods = ['GET', 'POST'])

def show_make_bet():

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT email FROM users WHERE logged = 1")
    email = cursor.fetchone()
    email2 = ' '.join([str(elem) for elem in email])

    if request.method == 'POST':
        home_score = int(request.form['home_score'])
        away_score = int(request.form['away_score'])
        game_id = request.form['game_id']
        group_id = request.form['id_group']
        Bet.make_bet(Bet(home_score, away_score, game_id, email2, group_id))
        return str(away_score)