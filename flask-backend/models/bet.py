import sqlite3
from services.utils import get_db_connection

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

        self.get_bet_winner()

        with get_db_connection() as bet_database_connection:
            try:
                database_cursor = bet_database_connection.cursor()
                database_cursor.execute('INSERT INTO bets (home_score, visitor_score, id_game, email, winner, score, group_) VALUES (?, ?, ?, ?, ?, ?, ?)',
                           (int(self.home_score), int(self.visitor_score), int(self.id_game), str(self.email), str(self.winner), 0, str(self.group_)))
                bet_database_connection.commit()          
            except:
                bet_database_connection.rollback()

        bet_database_connection.close()

    def get_bet_winner(self):
        if self.home_score > self.visitor_score:
            self.winner = "home"
        elif self.home_score < self.visitor_score:
            self.winner = "away"
        else:
            self.winner = "no"
