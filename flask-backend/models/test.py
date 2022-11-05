import sqlite3
import warnings
import pandas as pd
from services.utils import get_db_connection
from models.match import Match
#from pandas.core.common import SettingWithCopyWarning

#warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
#warnings.simplefilter(action='ignore', category=FutureWarning)

def score(real_home, real_away, real_winner, bet_home, bet_away, bet_winner, bet_user, id_game):
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

    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute('UPDATE bets SET score = ? WHERE email = ? and id_game == ?', (score, bet_user, id_game))
        cur.execute('UPDATE users SET score = score + ? WHERE email = ?', (score, bet_user))
        con.commit()


def bet_score():
    with get_db_connection() as con:
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

                score(real_home, real_away, real_winner, bet_home, bet_away, bet_winner, bet_user, id_game)

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