from flask import Blueprint, request
from services.utils import get_db_connection
from models.score import bet_score
from models.match import Match

register_result = Blueprint('register_result', __name__)
@register_result.route('/register_result', methods = ['GET', 'POST'])

def show_register_result():
    if request.method == 'POST':
        home_score = request.form['home_score']
        away_score = request.form['away_score']
        game_id = request.form['game_id']

        Match.register_final_score(home_score, away_score, game_id)
        bet_score()

        return 'OK'