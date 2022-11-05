from flask import Blueprint, request
from services.utils import get_db_connection
from models.test import bet_score
from models.match import Match

register_result = Blueprint('register_result', __name__)
@register_result.route('/register_result', methods = ['GET', 'POST'])

def show_register_result():
    if request.method == 'POST':
        home_score = request.form['home_score']
        away_score = request.form['away_score']
        game_id = request.form['game_id']

        #db = get_db_connection()
        #cur = db.cursor()
        #cur.execute("UPDATE matches SET final_score_home = '" + home_score + "', final_score_visitor = '" + away_score + "', is_over = 1 WHERE id_ = '" + game_id + "'")
        #db.commit()
        Match.register_final_score(home_score, away_score, game_id)
        bet_score()

        return 'OK'