from Human import Human
from Ai import AI
import random

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()
        self.player3 = AI()
        self.options=[]

    def display_greeting():
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print(" ")
        print("Heres how to play: ")
        print("Rock crushes Scissors, Rock crushes Lizard")
        print("Paper covers rock, Paper disproves Spock")
        print("Scissors cuts Paper, Scissors decapitates Lizard")
        print("Lizard poisons Spock, Lizard eats Paper")
        print("Spock vaporizes Rock, Spock smashes Scissors")
        print(" ")
        print("Winner will be determined by a best of 3.")

    def play_game():
        print("Choose Single player or Multiplayer")
        singlep=input(" ").upper
        if singlep=="SINGLE PLAYER":
            pass
        multi=input(" ").upper
        if multi=="MULTIPLAYER":
            pass



    def game_winner(self):
        pass

    def scoreboard(self):
        pass
        