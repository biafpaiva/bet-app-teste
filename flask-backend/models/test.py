from models.bet import Bet
from models.match import Match
import sqlite3


def score(real_home, real_away, real_winner, bet_home, bet_away, bet_winner, bet_user):
    '''Acertar placar exato 10;
        Acertar vencedor e um placar 6;
        Acertar vencedor ou empate não exato 3;
        Acertar apenas um placar 1; Não exato 0. *
        Oitavas e quartas de Final multiplica-se por 2; **
        Semi, disputa de terceiro e quarto lugar e final multiplica-se por 3.
         Obs: Os pontos não são acumulativos por jogo.'''
    score = 0
    if real_home == bet_home or real_away == bet_away:
        score = 1
    if real_winner == bet_winner or (real_winner == "no" and real_home != bet_home):
        score = 3
    if real_winner == bet_winner and (real_home == bet_home or real_away == bet_away) and real_winner != "no":
        score = 6
    if real_home == bet_home and real_away == bet_away and real_winner != "no":
        score = 10

    print(score)
    with sqlite3.connect('database/database.db') as con:
        cur = con.cursor()
        cur.execute('UPDATE bets SET score = ? WHERE email = ?', (score, bet_user))
        con.commit()


def bet_score():
    with sqlite3.connect('database/database.db') as con:
        cur = con.cursor()
        finished_game = list(cur.execute('SELECT * FROM matches WHERE is_over == 1'))

        for i in range(len(finished_game)):
            id_game = str(finished_game[i][0])
            real_home = finished_game[i][10]
            real_away = finished_game[i][11]
            real_winner = finished_game[i][13]

            bets_finished_game = list(cur.execute('SELECT * FROM bets WHERE id_game == ?', id_game))
            for j in range(len(bets_finished_game)):
                bet_home = bets_finished_game[j][1]
                bet_away = bets_finished_game[j][2]
                bet_user = bets_finished_game[j][4]
                bet_winner = bets_finished_game[j][5]
                print(bet_user)

                score(real_home, real_away, real_winner, bet_home, bet_away, bet_winner, bet_user)


Bet.make_bet(Bet(1, 2, 1, "bia"))
Bet.make_bet(Bet(1, 1, 1, "lana"))
Bet.make_bet(Bet(2, 1, 1, "cissa"))
Bet.make_bet(Bet(0, 0, 1, "outro"))

with sqlite3.connect('database/database.db') as con:
    cur = con.cursor()
    match_1 = Match(list(cur.execute('SELECT * FROM matches WHERE id_ == 1'))[0])

Match.register_final_score(match_1, 2, 1)
bet_score()