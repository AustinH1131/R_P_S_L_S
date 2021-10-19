from Player import Player

class Human(Player):
    def __init__(self):
        self.name = input('Enter Name Here: ')
        super().__init__()

   
    def select_gesture(self):
        print("Please choose: Rock, Paper, Scissors, Lizard, Spock")
        users_choice = input('Please enter a gesture: ').upper()
        while users_choice not in self.gestures:
            print('Invalid option. Try again')
            users_choice = input('Please enter a gesture: ').upper()
        self.selected_gesture = users_choice