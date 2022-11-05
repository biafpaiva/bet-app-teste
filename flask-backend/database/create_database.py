import sqlite3
import pandas as pd

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

df_jogos1 = pd.read_json("jogos-1.json")
for i in range(len(df_jogos1)):
    id = int(df_jogos1['id'][i])
    group_ = str(df_jogos1['group'][i])
    round = int(df_jogos1['round'][i])
    day_of_week = str(df_jogos1['weekDay'][i])
    date_ = str(df_jogos1['date'][i])
    time_ = str(df_jogos1['time'][i])
    stadium = str(df_jogos1['stadium'][i])
    teams = str(df_jogos1['teams'][i])
    home = str(df_jogos1['home'][i])
    visitor = str(df_jogos1['visitor'][i])
    final_score_home = 123
    final_score_visitor = 123
    is_over = 0
    winner = ""

    cur.execute(
        'INSERT INTO matches (id_, group_, round, day_of_week, date_, time_, stadium, teams, home, visitor, final_score_home, final_score_visitor, is_over, winner) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (id, group_, round, day_of_week, date_, time_, stadium, teams, home, visitor, final_score_home, final_score_visitor, is_over, winner))

df_jogosfinais = pd.read_json("jogos-finais.json")
for i in range(len(df_jogosfinais)):
    id = int(df_jogosfinais['id'][i])
    round = df_jogosfinais['round'][i]
    day_of_week = str(df_jogosfinais['weekDay'][i])
    date_ = str(df_jogosfinais['date'][i])
    time_ = str(df_jogosfinais['time'][i])
    stadium = str(df_jogosfinais['stadium'][i])
    teams = str(df_jogosfinais['teams'][i])
    home = str(df_jogosfinais['home'][i])
    visitor = str(df_jogosfinais['visitor'][i])

    cur.execute(
        'INSERT INTO matches_finals (id_, round, day_of_week, date_, time_, stadium, teams, home, visitor) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (id, round, day_of_week, date_, time_, stadium, teams, home, visitor))

cur.execute('INSERT INTO users (username, email, password) '
            'VALUES (?, ?, ?)',
            ("admin", "admin@admin.com", "eusouadm"))

connection.commit()
connection.close()