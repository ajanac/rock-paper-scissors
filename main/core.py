# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
# """
#  Rock Paper Scissors
# Rock Paper Scissors
#
# There are a number of functions that this program requires so let us have an overview of each.
#
# a random function: to generate rock, paper, or scissors.
# valid function: to check the validity of the move.
# result function: to declare the winner of the round.
# scorekeeper: to keep track of the score.
# The program requires the user to make the first move before it makes one the move.
# Once the move is validated the input is evaluated, the input entered could be a string or an alphabet.
# After evaluating the input string a winner is decided by the result function and the score of the round is updated by the scorekeeper function.
#
# """

""" Rock Paper Scissors
----------------------------------------
"""
import logging

import random
import re

from helpers import Utils
from player import Player

logger = logging.getLogger(__name__)
global_score = 0


def score_keeper():
    pass


def valid(user_hoice):
    if not re.match("[SsRrPp]", user_hoice):
        return True
    else:
        return False


def result(opponent_choice, user_choice):
    if opponent_choice == str.upper(user_choice):
        result_string = "Tie"
    elif opponent_choice == 'R' and user_choice.upper() == 'S':
        result_string = "Scissors beats rock, I win!"
    elif opponent_choice == 'S' and user_choice.upper() == 'P':
        result_string = "Scissors beats paper! I win!"
    elif opponent_choice == 'P' and user_choice.upper() == 'R':
        result_string = "Paper beat rock, I win!"
    else:
        result_string = "you win!"
    return result_string


def start_game():
    util_obj = Utils()
    player_one_name = util_obj.get_player_name()
    print(player_one_name)
    player_one = Player(player_one_name, 0)
    player_two= Player("System", 0)
    while 1 < 2:
        print("\n*****************************")
        print("Rock, Paper, Scissors - Game!!!")
        print("\n*****************************")
        user_choice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
        if valid(user_choice):
            print("Please choose a letter:")
            print("[R]ock, [S]cissors or [P]aper.")
            continue
        print("your choice: ", user_choice)
        choices = ['R', 'P', 'S']
        opponent_choice = random.choice(choices)
        result_string = result(opponent_choice, user_choice)
        print(result_string)


if __name__ == '__main__':
    start_game()
