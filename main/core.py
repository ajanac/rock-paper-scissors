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
from player import Player
from utils import Utils

import logging
import random
import re

logger = logging.getLogger(__name__)

def valid_user_choice(user_choice):
    if not re.match("[SsRrPp]", user_choice):
        return True
    else:
        return False

def start_game():
    util_obj = Utils()
    choices = ['R', 'P', 'S']
    player_one_name = util_obj.get_player_name()
    print(player_one_name)
    player_one = Player(player_one_name, 0)
    player_two = Player("System", 0)
    while True:
        print("\n*****************************")
        print("Rock, Paper, Scissors - Game!!!")
        print("\n*****************************")
        player_one_choice = input("Choose your weapon [R]ock | [P]aper | [S]cissors: ")
        if valid_user_choice(player_one_choice):
            print("You choose an invalid input")
            print("Please choose a valid letter:")
            print("[R]ock | [S]cissors | [P]aper.")
            continue
        print(f"your choice: {player_one_choice}")
        logger.info(f"your choice: {player_one_choice}")
        player_two_choice = random.choice(choices)
        print(f"opponent choice: {player_two_choice}")
        util_obj.score_keep(player_one, player_one_choice.upper(), player_two, player_two_choice)
        wanna_play_again = input("Do you want to continue [Y]es | [N]o ?")
        if wanna_play_again.upper() == 'Y':
            continue
        else:
            (winner_name, winner_score) = util_obj.winner(player_one, player_two)
            if winner_name != "Tie":
                print(f"Winner is {winner_name} and score is {winner_score}")
            else:
                print("It is a tie")
            break

if __name__ == '__main__':
    start_game()
