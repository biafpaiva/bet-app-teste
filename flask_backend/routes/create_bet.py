from flask import Blueprint, request

create_bet = Blueprint('create_bet', __name__)
@create_bet.route('/create_bet', methods = ['POST'])

def show_create_bet():
    if request.method == 'POST' and 'mandante_placar' in request.form and 'password' in request.form:
        mandante_placar = request.form['username']
        password = request.form['password']
    return 'bet endpoint'

    #visitante