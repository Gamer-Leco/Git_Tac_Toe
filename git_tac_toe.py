# Projet : Git_Tac_Toe
# Auteurs : Ilan, Leo
# Cours : MA-24
# Version : 1.0

import random as r
import os
import time

def clear_console():
  os.system("cls" if os.name == "nt" else "clear")

def start_game():
  global grid, player_x, player_o, turn, mode_play, game_state, score_x, score_o, computer