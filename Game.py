from Human import Human
from Ai import AI
import random

class Game:
    def __init__(self,):
        self.player1 = Human()
        self.player2 = Human()
        self.player3 = AI()
        self.gestures=["Rock","Paper","Scissors","Lizard","Spock"]

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

    def play_game(self,player1_gesture,player2_gesture,player3_gesture,player1wins,player2wins,player3wins):
        print("Choose Single player or Multiplayer")
        singlep=input(" ").upper
        if singlep=="SINGLE PLAYER":
            singlep=True
            winner=False
        while winner==False:
            if player1_gesture=="Rock" and player3_gesture=="Lizard" or "Scissor":
                print(player1_gesture)
                player1wins+1
            elif player3_gesture=="Rock" and player1_gesture=="Lizard" or "Scissor":
                print(player3_gesture)
                player3wins+1
            elif player1_gesture=="Paper" and player3_gesture=="Rock" or "Spock":
                print(player1_gesture)
                player1wins+1
            elif player3_gesture=="Paper" and player1_gesture=="Rock" or "Spock":
                print(player3_gesture)
                player3wins+1
            elif player1_gesture=="Scissors" and player3_gesture=="Paper" or "Lizard":
                print(player1_gesture)
                player1wins+1
            elif player3_gesture=="Scissors" and player1_gesture=="Paper" or "Lizard":
                print(player3_gesture)
                player3wins+1   
            elif player1_gesture=="Lizard" and player3_gesture=="Paper" or "Spock":
                print(player1_gesture)
                player1wins+1
            elif player3_gesture=="Lizard" and player1_gesture=="Paper" or "Spock":
                print(player3_gesture)
                player3wins+1
            elif player1_gesture=="Spock" and player3_gesture=="Rock" or "Scissors":
                print(player1_gesture)
                player1wins+1
            elif player3_gesture=="Spock" and player1_gesture=="Rock" or "Scissors":
                print(player3_gesture)
                player3wins+1
            elif player1_gesture==player3_gesture:
                print("Draw! Rematch!")
                return 
                
            if  player1wins==2:
                winner=True
            elif player3wins==2:
                winner=True
            



        multi=input(" ").upper
        if multi=="MULTIPLAYER":
              winner=False
        while winner==False:
            if player1_gesture=="Rock" and player2_gesture=="Lizard" or "Scissor":
                print(player1_gesture)
                player1wins+1
            elif player2_gesture=="Rock" and player1_gesture=="Lizard" or "Scissor":
                print(player2_gesture)
                player2wins+1
            elif player1_gesture=="Paper" and player2_gesture=="Rock" or "Spock":
                print(player1_gesture)
                player1wins+1
            elif player2_gesture=="Paper" and player1_gesture=="Rock" or "Spock":
                print(player2_gesture)
                player2wins+1
            elif player1_gesture=="Scissors" and player2_gesture=="Paper" or "Lizard":
                print(player1_gesture)
                player1wins+1
            elif player2_gesture=="Scissors" and player1_gesture=="Paper" or "Lizard":
                print(player2_gesture)
                player2wins+1    
            elif player1_gesture=="Lizard" and player2_gesture=="Paper" or "Spock":
                print(player1_gesture)
                player1wins+1
            elif player2_gesture=="Lizard" and player1_gesture=="Paper" or "Spock":
                print(player2_gesture)
                player2wins+1
            elif player1_gesture=="Spock" and player2_gesture=="Rock" or "Scissors":
                print(player1_gesture)
                player1wins+1
            elif player2_gesture=="Spock" and player1_gesture=="Rock" or "Scissors":
                print(player2_gesture)
                player2wins+1
            elif player1_gesture==player2_gesture:
                print("Draw! Rematch!")
                return 
            
            if  player1wins==2:
                winner=True
            elif player2wins==2:
                winner=True

    def select_gesture(self,singlep):
        if singlep==False:
             print("Choose one of the following: ")
             print(self.gestures) 
             player1_gesture = input(" ")
             player2_gesture = input(" ")

        elif singlep==True:  
            print("Choose one of the following: ")
            print(self.gestures) 
            player1_gesture = input(" ")
            player3_gesture = random.choice(self.gestures)
       

    def game_winner(self):
        pass

    def scoreboard(self):
        player1wins=0
        player2wins=0
        player3wins=0
        

