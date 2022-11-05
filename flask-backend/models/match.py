import sqlite3

class Match:
    def __init__(self, list):
        self.id = list[0]
        self.group = list[1]
        self.round = list[2]
        self.weekDay = list[3]
        self.date = list[4]
        self.time = list[5]
        self.stadium = list[6]
        self.teams = list[7]
        self.home = list[8]
        self.visitor = list[9]
        self.final_score_home = list[10]
        self.final_score_visitor = list[11]
        self.is_over = list[12]
        self.winner = list[13]

    def register_final_score(final_score_home, final_score_visitor, game_id):
        if final_score_home > final_score_visitor:
            winner = "home"
        if final_score_home < final_score_visitor:
            winner = "away"
        if final_score_home == final_score_visitor:
            winner = "no"

        with sqlite3.connect('database/database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('UPDATE matches SET final_score_home = ?, final_score_visitor = ?, is_over = ?, winner = ? WHERE id_ = ?',
                            (final_score_home, final_score_visitor, 1, winner, int(game_id)))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()

        return msg