import sqlite3

class Bet:
    def __init__(self, home_score, visitor_score, id_game, email, group):
        self.home_score = home_score
        self.visitor_score = visitor_score
        self.winner = ""
        self.id_game = id_game
        self.email = email
        self.score = 0
        self.group_ = group

    def make_bet(self):
        home_score = self.home_score
        visitor_score = self.visitor_score
        id_game = self.id_game
        email = self.email

        if home_score > visitor_score:
            self.winner = "home"
        if home_score < visitor_score:
            self.winner = "away"
        if home_score == visitor_score:
            self.winner = "no"

        with sqlite3.connect('database/database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score, group_) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (int(home_score), int(visitor_score), int(id_game), str(email), str(self.winner), 0, str(self.group_)))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()

        return 