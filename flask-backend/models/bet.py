import sqlite3

class Bet:
    def __init__(self, home_score, visitor_score, id_game, email):
        self.home_score = home_score
        self.visitor_score = visitor_score
        self.id_game = id_game
        self.email = email
        self.score = 0

    def make_bet(self):
        home_score = self.home_score
        visitor_score = self.visitor_score
        id_game = self.id_game
        email = self.email

        if home_score > visitor_score:
            winner = "home"
        if home_score < visitor_score:
            winner = "away"
        if home_score == visitor_score:
            winner = "no"

        with sqlite3.connect('database/database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score) VALUES (?, ?, ?, ?, ?, ?)',
                            (int(home_score), int(visitor_score), int(id_game), str(email), winner, 0))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()

        return msg