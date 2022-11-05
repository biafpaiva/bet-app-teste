from flask import Blueprint, send_file

list_matches = Blueprint('list_matches', __name__)
@list_matches.route('/list_matches', methods = ['GET'])

def show_list_matches():
    games = send_file('database/jogos-1.json')
    games.headers.add("Access-Control-Allow-Origin", "*")
    return games