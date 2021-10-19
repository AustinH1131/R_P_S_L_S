from Player import Player
import random
class AI(Player):
    def __init__(self):
        self.name="Computer"
        super().__init__()
   
   
    def select_gesture(self):
        self.selected_gesture = random.choice(self.gestures)