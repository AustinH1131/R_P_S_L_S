from Game import Game
import random

game = Game()
player1_gesture=game.select_gesture.player1_gesture
player2_gesture=game.select_gesture.player2_gesture
player3_gesture=game.select_gesture.player3_gesture
player1wins=game.game_winner.player1wins
player2wins=game.game_winner.player2wins
player3wins=game.game_winner.player3wins
game.display_greeting()
game.play_game(player1_gesture, player2_gesture, player3_gesture, player1wins, player2wins,player3wins)




