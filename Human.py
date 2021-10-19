from Player import Player

class Human(Player):
    def __init__(self):
        self.name = input('Enter Name Here: ')
        super().__init__()

   
    def select_gesture(self):
        print("Please choose: Rock, Paper, Scissors, Lizard, Spock")
        self.selected_gesture = input('Please enter a gesture: ').upper()
        # while users_choice is not self.gestures:
        #     print('Invalid option. Try again')
        #     users_choice = input('Please enter a gesture: ').upper()
        # self.selected_gesture = users_choice