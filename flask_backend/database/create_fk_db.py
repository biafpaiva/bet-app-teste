import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

'''
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('mrsbolinhu', 'ilana@email.com', 'boloehtudo'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('cissakind', 'cissa@email.com', 'polly'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('biaf', 'bia@email.com', 'gatinhos'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('andreh', 'andre@email.com', 'software'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('eduardo', 'eduardo@email.com', 'sommerville'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('mateus', 'mateus@email.com', 'bettercaul'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('sololimones', 'sasa@email.com', 'pinklemonade'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('sacoman', 'gabriel@email.com', 'sacomano'))
cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', ('augusto', 'guto@email.com', 'cabuloso'))
'''
cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score) VALUES (?, ?, ?, ?, ?, ?)', 
            (1, 2, 3, 'ilana@email.com', 'away', 0))
cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score) VALUES (?, ?, ?, ?, ?, ?)',
            (1, 1, 3, 'cissa@email.com', 'no', 0))
cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score) VALUES (?, ?, ?, ?, ?, ?)',
            (0, 2, 2, 'ilana@email.com', 'away', 0))
cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score) VALUES (?, ?, ?, ?, ?, ?)',
            (1, 2, 8, 'ilana@email.com', 'away', 0))
cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score) VALUES (?, ?, ?, ?, ?, ?)',
            (2, 2, 7, 'ilana@email.com', 'no', 0))
cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score) VALUES (?, ?, ?, ?, ?, ?)',
            (6, 2, 1, 'ilana@email.com', 'home', 0))

con.commit()
con.close()