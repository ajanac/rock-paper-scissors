class Utils():
    # displays a prompt and reads in the players name returning a string
    def get_player_name(self):
        # needs code here, see next function for idea of what
        player_name = input("Hello, What is your name?")
        return player_name

    # ask the player to make a choice, takes a Player object
    # and returns a string
    def get_player_choice(self, player):
        print("%s, what do you choose?" % player.name)
        return input("> ")

    # determines who wins and updates score accordingly
    # takes in the player objects and their attack choices
    def attack(player1, choice1, player2, choice2):
        if choice1 == choice2:
            print ("Its's a tie.")
        elif choice1 == "1" and choice2 == "2":
            print ("%s wins." % player2)
            player2.score = player2.score + 1
        elif ...  # other attacks
    """
    https://stackoverflow.com/questions/6539860/how-do-i-keep-score-in-a-rock-paper-scissors-game
    https://stackoverflow.com/questions/23238352/create-object-from-class-in-separate-file
    """