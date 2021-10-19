from Human import Human
from Ai import AI
import random
from Player import Player

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()
        self.player2.select_gesture()
        self.winner = False

    def display_greeting(self):
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

    def choose_game_mode(self):
        user_input = input('Please enter 1 for single player and 2 for multiplayer: ')
        if user_input == '1':
            self.player1 = Human()
            self.player2 = AI()
        elif user_input == '2':
            self.player1 = Human()
            self.player2 = Human()

    def play_game(self):
        self.winner=False
        self.player1.wins = 0
        self.player2.wins= 0
      
        while self.winner==False: 
            self.player1.select_gesture()
            self.player2.select_gesture()
    
            if self.player1.selected_gesture=="Rock" and (self.player2.selected_gesture=="Lizard" or self.player2.selected_gesture=="Scissors"):
                print(self.player1.selected_gesture)
                self.player1.wins+1
            elif self.player2.selected_gesture=="Rock" and (self.player1.selected_gesture=="Lizard" or self.player1.selected_gesture=="Scissors"):
                print(self.player2.selected_gesture)
                self.player2.wins+1
            elif self.player1.selected_gesture=="Paper" and (self.player2.selected_gesture=="Rock" or self.player2.selected_gesture=="Spock"):
                print(self.player1.selected_gesture)
                self.player1.wins+1
            elif self.player2.selected_gesture=="Paper" and (self.player1.selected_gesture=="Rock" or self.player1.selected_gesture=="Spock"):
                print(self.player2.selected_gesture)
                self.player2.wins+1
            elif self.player1.selected_gesture=="Scissors" and (self.player2.selected_gesture=="Paper" or self.player2.selected_gesture=="Lizard"):
                print(self.player1.selected_gesture)
                self.player1.wins+1
            elif self.player2.selected_gesture=="Scissors" and (self.player1.selected_gesture=="Paper" or self.player1.selected_gesture=="Lizard"):
                print(self.player2.selected_gesture)
                self.player2.wins+1    
            elif self.player1.selected_gesture=="Lizard" and (self.player2.selected_gesture=="Paper" or self.player2.selected_gesture=="Spock"):
                print(self.player1.selected_gesture)
                self.player1.wins+1
            elif self.player2.selected_gesture=="Lizard" and (self.player1.selected_gesture=="Paper" or self.player1.selected_gesture=="Spock"):
                print(self.player2.selected_gesture)
                self.player2.wins+1
            elif self.player1.selected_gesture=="Spock" and (self.player2.selected_gesture=="Rock" or self.player2.selected_gesture=="Scissors"):
                print(self.player1.selected_gesture)
                self.player1.wins+1
            elif self.player2.selected_gesture=="Spock" and (self.player1.selected_gesture=="Rock" or self.player1.selected_gesture=="Scissors"):
                print(self.player2.selected_gesture)
                self.player2.wins+1
            elif self.player1.selected_gesture==self.player2.selected_gesture:
                print("Draw! Rematch!")
                
            if  self.player1.wins==2:
                print(self.player1.wins,"/",self.player2.wins)
                self.winner = True
            elif self.player2.wins==2:
                print(self.player1.wins,"/",self.player2.wins)
                self.winner=True  
    
    def game_winner(self):  
        if self.player1.wins==2:
            print(self.player1.name,"Wins!")
        if self.player2.wins==2:
            print(self.player2.name, "Wins!")   
    
    def run(self):
        self.display_greeting()
        self.choose_game_mode()
        self.play_game()
        self.game_winner()
    
        

