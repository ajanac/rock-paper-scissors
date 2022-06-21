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
import random
import re

def startGame():
    while (1 < 2):
        print("\n")
        print("Rock, Paper, Scissors - Go!!!")
        user_choice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
        if not re.match("[SsRrPp]", user_choice):
            print("Please choose a letter:")
            print("[R]ock, [S]cissors or [P]aper.")
            continue
        print("your choice: ", user_choice)
        choices = ['R', 'P', 'S']
        opponent_choice = random.choice(choices)
        if opponent_choice == str.upper(user_choice):
            print("Tie!")
        elif opponent_choice == 'R' and user_choice.upper() == 'S':
            print("Scissors beats rock, I win!")
            continue
        elif opponent_choice == 'S' and user_choice.upper() == 'P':
            print("Scissors beats paper! I win!")
            continue
        elif  opponent_choice == 'P' and user_choice.upper() == 'R':
            print("Paper beat rock, I win!")
            continue
        else:
            print("you win!")

if __name__ == '__main__':
    startGame()




