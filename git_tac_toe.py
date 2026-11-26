# Projet : Git_Tac_Toe
# Auteurs : Ilan, Leo
# Cours : MA-24
# Version : 1.0

import random as r
import os
import time

title = "Git tac toe"

def clear_console():
  os.system("cls" if os.name == "nt" else "clear")

def start_game():
  global grid, player_x, player_o, turn, mode_play, game_state, score_x, score_o, computer

  grid = [str(i) for i in range(1, 10)]
  player_x = ""
  player_o = ""
  score_x = 0
  score_o = 0
  game_state = "running"
  turn = r.choice(["X", "O"])
  computer = False

  clear_console()
  print("----- " + title + " -----")
  input("\nAppuyez sur <Enter> pour commencer !")

  while True:
    clear_console()
    print("----- Menu -----\n")
    print("1. Joueur contre Joueur")
    print("2. Joueur contre ordinateur")
    print("3. Quitter\n")

    mode_play = input("Choisir un mode (1-3) : ")

    if mode_play in ["1", "2", "3"]:
      break

    print("\n[ERREUR] Choix invalide !")
    time.sleep(1.5)

  if mode_play == "3":
    return

  computer = mode_play == "2"

  if computer:
    player_x = input("\nEntrez votre nom (X) : ").strip()
    player_o = "Ordinateur"
  else:
    player_x = input("\nEntrez le nom du joueur X : ").strip()
    player_o = input("Entrez le nom du joueur O : ").strip()

  if not player_x:
    player_x = "Joueur 1"

  if not player_o:
    player_o = "Joueur 2"

  #jouer_tour()