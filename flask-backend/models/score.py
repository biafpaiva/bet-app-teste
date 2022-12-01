import sqlite3
import warnings
import pandas as pd
from services.utils import get_db_connection
from models.match import Match


def is_perfect_bet(real_home, bet_home, real_away, bet_away):
    return real_home == bet_home and real_away == bet_away

def is_correct_winner_partial_result(real_winner, bet_winner, real_home, bet_home, real_away, bet_away):
    return real_winner == bet_winner and (real_home == bet_home or real_away == bet_away) and real_winner != "no"

def is_correct_winner_wrong_result(real_winner, bet_winner, real_home, bet_home):
    return real_winner == bet_winner or (real_winner == "no" and real_home != bet_home)

def is_wrong_winner_partial_result(real_home, bet_home, real_away, bet_away):
    return real_home == bet_home or real_away == bet_away

def calculate_user_score(real_winner, bet_winner, real_home, bet_home, real_away, bet_away):
    if is_perfect_bet(real_home, bet_home, real_away, bet_away):
        return 10
    if is_correct_winner_partial_result(real_winner, bet_winner, real_home, bet_home, real_away, bet_away):
        return 6
    if is_correct_winner_wrong_result(real_winner, bet_winner, real_home, bet_home):
        return 3
    if is_wrong_winner_partial_result(real_home, bet_home, real_away, bet_away):
        return 1
    return 0

def register_user_score(real_home, real_away, real_winner, bet_home, bet_away, bet_winner, bet_user, id_game):

    user_score = calculate_user_score(real_winner, bet_winner, real_home, bet_home, real_away, bet_away)
    print(user_score)
    with get_db_connection() as bet_database_connection:
        database_cursor = bet_database_connection.cursor()
        database_cursor.execute('UPDATE bets SET score = ? WHERE email = ? and id_game == ?', (user_score, bet_user, id_game))
        database_cursor.execute('UPDATE users SET score = score + ? WHERE email = ?', (user_score, bet_user))
        bet_database_connection.commit()


def bet_score():
    with get_db_connection() as con:
        cur = con.cursor()
        finished_game = list(cur.execute('SELECT * FROM matches WHERE is_over == 1'))

        for i in range(len(finished_game)):
            id_game = str(finished_game[i][0])
            real_home = finished_game[i][10]
            real_away = finished_game[i][11]
            real_winner = finished_game[i][13]

            bets_finished_game = list(cur.execute('SELECT * FROM bets WHERE id_game == ?', (id_game, )))
            for j in range(len(bets_finished_game)):
                bet_home = bets_finished_game[j][1]
                bet_away = bets_finished_game[j][2]
                bet_user = bets_finished_game[j][4]
                bet_winner = bets_finished_game[j][5]

                register_user_score(real_home, real_away, real_winner, bet_home, bet_away, bet_winner, bet_user, id_game)

def calc_teams_score(df, df_countrys):
    '''São oito grupos e as duas equipes mais bem colocadas destas classificam-se para os oitavos de final,
        Quem ganha = 3pts
        Quem empata = 1pt
        Quem perde = 0pt'''
    new_df = df_countrys.copy()
    for i in range(len(df)):
        winner_country = df['winner_name'][i]
        loser_country = df['loser_name'][i]
        if winner_country != 'no':
            new_df.loc[new_df['home'] == winner_country, 'team_score'] += 3
            new_df.loc[new_df['home'] == loser_country, 'team_score'] += 0
        else:
            new_df.loc[new_df['home'] == loser_country, 'team_score'] += 1
            new_df.loc[new_df['home'] == winner_country, 'team_score'] += 1

    return new_df

def oitavas(user_email):
    with get_db_connection() as con:
        cur = con.cursor()

    bets = list(cur.execute('SELECT * FROM bets WHERE email = ?', [user_email]))
    df_bets = pd.DataFrame(bets).rename(columns={1: 'home_score', 2: 'visitor_score', 3:'id_game', 4: 'email', 5: 'winner', 6: 'score', 7: 'group'}).drop(0, axis=1)
    df_jogos1 = pd.read_json("/database/jogos-1.json").filter(['id', 'home', 'visitor']).rename(columns={'id':'id_game'})
    df = pd.merge(df_bets, df_jogos1, on=['id_game'])
    df_countrys = pd.DataFrame(df.filter(['group', 'home'])).drop_duplicates()
    df_countrys['team_score'] = 0
    df['winner_name'] = 'n'
    df['loser_name'] = 'n'
    for i in range(len(df)):
        if df['winner'][i] == 'away':
            df['winner_name'][i] = df['visitor'][i]
            df['loser_name'][i] = df['home'][i]
        if df['winner'][i] == 'home':
            df['winner_name'][i] = df['home'][i]
            df['loser_name'][i] = df['visitor'][i]
        if df['winner'][i] == 'no':
            df['winner_name'][i] = 'no'
            df['loser_name'][i] = 'no'

    new_df = calc_teams_score(df, df_countrys).groupby(['group'])['team_score', 'home'].apply(lambda x: x.nlargest(2, columns=['team_score']))
    return new_df.droplevel(0)['home'].to_list()

def points_by_teams(teams_passed, user_email):
    teams_bet = oitavas(user_email)
    new_points = len([w for w in teams_bet if w in teams_passed])
    return(new_points)

def sum_all_bets_scores(user_email):
    with get_db_connection() as con:
        cur = con.cursor()

    score_by_bets = list(cur.execute('SELECT score FROM bets WHERE email = ?', [user_email]))
    res = [sum(i) for i in zip(*score_by_bets)]
    return res