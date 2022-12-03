import pytest
from flask_backend.models.score import *
from flask_backend.models.bet import Bet

def test_calculate_perfect_score():
	user_score = calculate_user_score('Brasil', 'Brasil', 1, 1, 0, 0)
	assert(user_score == 10)

def test_calculate_correct_winner_partial_result():
	user_score = calculate_user_score('Brasil', 'Brasil', 2, 2, 1, 0)
	assert(user_score == 6)

def test_calculate_correct_winner_wrong_result():
	user_score = calculate_user_score('Brasil', 'Brasil', 3, 2, 1, 0)
	assert(user_score == 3)

def test_calculate_wrong_winner_partial_result():
	user_score = calculate_user_score('Brasil', 'Argentina', 3, 3, 1, 4)
	assert(user_score == 1)

def test_calculate_wrong_bet():
	user_score = calculate_user_score('Argentina', 'Brasil', 3, 2, 1, 0)
	assert(user_score == 0)

def test_user_score_after_first_bet():

	user_email = 'User@email'
	Bet.make_bet(Bet(1, 0, 5, user_email, 0))

	Match.register_final_score(1, 0, 5)
	bet_score()

	score = sum_all_bets_scores(user_email)
	assert(score == [10])

def test_user_score_after_multiple_bets():

	user_email = 'User2@email'
	Bet.make_bet(Bet(1, 0, 1, user_email, 0))
	Bet.make_bet(Bet(1, 0, 2, user_email, 0))
	Bet.make_bet(Bet(1, 0, 3, user_email, 0))
	Bet.make_bet(Bet(1, 0, 4, user_email, 0))

	Match.register_final_score(1, 0, 1)
	Match.register_final_score(0, 1, 2)
	Match.register_final_score(3, 0, 3)
	Match.register_final_score(1, 1, 4)
	bet_score()

	score = sum_all_bets_scores(user_email)
	assert(score == [17])

def test_score_after_terrible_sequence_bets():
	user_email = 'User3@email'
	Bet.make_bet(Bet(1, 0, 6, user_email, 0))
	Bet.make_bet(Bet(1, 0, 7, user_email, 0))
	Bet.make_bet(Bet(1, 0, 8, user_email, 0))
	Bet.make_bet(Bet(1, 0, 9, user_email, 0))

	Match.register_final_score(0, 1, 6)
	Match.register_final_score(0, 1, 7)
	Match.register_final_score(0, 3, 8)
	Match.register_final_score(0, 7, 9)
	bet_score()

	score = sum_all_bets_scores(user_email)
	assert(score == [0])

def test_score_after_perfect_sequence_bets():
	user_email = 'User4@email'
	Bet.make_bet(Bet(1, 0, 10, user_email, 0))
	Bet.make_bet(Bet(1, 0, 11, user_email, 0))
	Bet.make_bet(Bet(1, 0, 12, user_email, 0))
	Bet.make_bet(Bet(1, 0, 13, user_email, 0))

	Match.register_final_score(1, 0, 10)
	Match.register_final_score(1, 0, 11)
	Match.register_final_score(1, 0, 12)
	Match.register_final_score(1, 0, 13)
	bet_score()

	score = sum_all_bets_scores(user_email)
	assert(score == [40])
