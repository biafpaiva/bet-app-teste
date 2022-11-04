import sqlite3
import pandas as pd

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

df = pd.read_json("jogos-1.json")
for i in range(len(df)):
    id = int(df['id'][i])
    group_ = str(df['group'][i])
    round = int(df['round'][i])
    day_of_week = str(df['weekDay'][i])
    date_ = str(df['date'][i])
    time_ = str(df['time'][i])
    stadium = str(df['stadium'][i])
    teams = str(df['teams'][i])
    home = str(df['home'][i])
    visitor = str(df['visitor'][i])
    final_score_home = 123
    final_score_visitor = 123
    is_over = 0
    winner = ""

    cur.execute(
        'INSERT INTO matches (id_, group_, round, day_of_week, date_, time_, stadium, teams, home, visitor, final_score_home, final_score_visitor, is_over, winner) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (id, group_, round, day_of_week, date_, time_, stadium, teams, home, visitor, final_score_home, final_score_visitor, is_over, winner))


connection.commit()
connection.close()