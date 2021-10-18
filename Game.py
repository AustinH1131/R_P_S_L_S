from Human import Human
from Ai import AI
import random

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()
        self.player3 = AI()
        self.gestures=["Rock","Paper","Scissors","Lizard","Spock"]
        self.winner=False
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

    def play_game(self,):
        print("Choose Single player or Multiplayer")
        singlep=input(" ").upper()
        if singlep=="SINGLE PLAYER":
            singlep=True
            while self.winner==False:
                self.select_gesture(True)
                if self.player1.selected_gesture=="Rock" and (self.player3.selected_gesture=="Lizard" or self.player3.selected_gesture=="Scissor"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player3.selected_gesture=="Rock" and (self.player1.selected_gesture=="Lizard" or self.player1.selected_gesture=="Scissor"):
                    print(self.player3.selected_gesture)
                    self.player3.wins+=1
                elif self.player1.selected_gesture=="Paper" and (self.player3.selected_gesture=="Rock" or self.player3.selected_gesture=="Spock"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player3.selected_gesture=="Paper" and (self.player1.selected_gesture=="Rock" or self.player1.selected_gesture=="Spock"):
                    print(self.player3.selected_gesture)
                    self.player3.wins+=1
                elif self.player1.selected_gesture=="Scissors" and (self.player3.selected_gesture=="Paper" or self.player3.selected_gesture=="Lizard"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player3.selected_gesture=="Scissors" and (self.player1.selected_gesture=="Paper" or self.player1.selected_gesture=="Lizard"):
                    print(self.player3.selected_gesture)
                    self.player3.wins+=1   
                elif self.player1.selected_gesture=="Lizard" and (self.player3.selected_gesture=="Paper" or self.player3.selected_gesture=="Spock"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player3.selected_gesture=="Lizard" and (self.player1.selected_gesture=="Paper" or self.player1.selected_gesture=="Spock"):
                    print(self.player3.selected_gesture)
                    self.player3.wins+=1
                elif self.player1.selected_gesture=="Spock" and (self.player3.selected_gesture=="Rock" or self.player3.selected_gesture=="Scissors"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player3.selected_gesture=="Spock" and (self.player1.selected_gesture=="Rock" or self.player1.selected_gesture=="Scissors"):
                    print(self.player3.selected_gesture)
                    self.player3.wins+=1
                elif self.player1.selected_gesture==self.player3.selected_gesture:
                    print("Draw! Rematch!")
                    return 
                    
                if  self.player1.wins==2:
                    print(self.player1.wins,"/",self.player3.wins)
                    self.winner=True
                elif self.player3.wins==2:
                    print(self.player1.wins,"/",self.player3.wins)
                    self.winner=True
            

      
        elif singlep=="MULTIPLAYER":
            self.winner=False
            while self.winner==False:
                self.select_gesture(False)
                if self.player1.selected_gesture=="Rock" and (self.player2.selected_gesture=="Lizard" or self.player2.selected_gesture=="Scissors"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player2.selected_gesture=="Rock" and (self.player1.selected_gesture=="Lizard" or self.player1.selected_gesture=="Scissors"):
                    print(self.player2.selected_gesture)
                    self.player2.wins+=1
                elif self.player1.selected_gesture=="Paper" and (self.player2.selected_gesture=="Rock" or self.player2.selected_gesture=="Spock"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player2.selected_gesture=="Paper" and (self.player1.selected_gesture=="Rock" or self.player1.selected_gesture=="Spock"):
                    print(self.player2.selected_gesture)
                    self.player2.wins+=1
                elif self.player1.selected_gesture=="Scissors" and (self.player2.selected_gesture=="Paper" or self.player2.selected_gesture=="Lizard"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player2.selected_gesture=="Scissors" and (self.player1.selected_gesture=="Paper" or self.player1.selected_gesture=="Lizard"):
                    print(self.player2.selected_gesture)
                    self.player2.wins+=1    
                elif self.player1.selected_gesture=="Lizard" and (self.player2.selected_gesture=="Paper" or self.player2.selected_gesture=="Spock"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player2.selected_gesture=="Lizard" and (self.player1.selected_gesture=="Paper" or self.player1.selected_gesture=="Spock"):
                    print(self.player2.selected_gesture)
                    self.player2.wins+=1
                elif self.player1.selected_gesture=="Spock" and (self.player2.selected_gesture=="Rock" or self.player2.selected_gesture=="Scissors"):
                    print(self.player1.selected_gesture)
                    self.player1.wins+=1
                elif self.player2.selected_gesture=="Spock" and (self.player1.selected_gesture=="Rock" or self.player1.selected_gesture=="Scissors"):
                    print(self.player2.selected_gesture)
                    self.player2.wins+=1
                elif self.player1.selected_gesture==self.player2.selected_gesture:
                    print("Draw! Rematch!")
                    return 
                
                if  self.player1.wins==2:
                    print(self.player1.wins,"/",self.player2.wins)
                    self.winner=True
                elif self.player2.wins==2:
                    print(self.player1.wins,"/",self.player2.wins)
                    self.winner=True

    def select_gesture(self,singlep):
        if singlep==False:
            print("Choose one of the following: ")
            print(self.gestures) 
            self.selected_gesture=" "
            self.player1.selected_gesture = input(" ")
             
            self.player2.selected_gesture = input(" ")
            self.player2.selected_gesture
        elif singlep==True:  
            print("Choose one of the following: ")
            print(self.gestures) 
            self.player1.selected_gesture = input(" ")
            self.player3.selected_gesture = random.choice(self.gestures)
            self.player3.selected_gesture    
    
    def game_winner(self,):  
        if self.player1.wins==2:
            print(self.player1.name,"Wins!")
        if self.player2.wins==2:
            print(self.player2.name, "Wins!")   
        if self.player3.wins==2:
            print(self.player3.name, "Wins!") 
        

