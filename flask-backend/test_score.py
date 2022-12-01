from models.score import *

class Test_score():

	def test_perfect_score(self):
		user_score = calculate_user_score('Brasil', 'Brasil', 1, 1, 0, 0)
		assert(user_score == 10)

	def test_correct_winner_partial_result(self):
		user_score = calculate_user_score('Brasil', 'Brasil', 2, 2, 1, 0)
		assert(user_score == 6)

	def test_correct_winner_wrong_result(self):
		user_score = calculate_user_score('Brasil', 'Brasil', 3, 2, 1, 0)
		assert(user_score == 3)

	def test_wrong_winner_partial_result(self):
		user_score = calculate_user_score('Brasil', 'Argentina', 3, 3, 1, 4)
		assert(user_score == 1)

	def test_wrong_bet(self):
		user_score = calculate_user_score('Argentina', 'Brasil', 3, 2, 1, 0)
		assert(user_score == 0)


