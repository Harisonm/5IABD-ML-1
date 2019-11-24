import pygame
from acteurs import *
from agents import TabQLearningAgent
from affichage import Afficheur
from runners import run_step

FRAME_RATE = 30
SCREEN_W, SCREEN_H = 232, 272

gs = PacmanArena(SCREEN_W, SCREEN_H)
pacman = PacMan(gs, 108, 184)

playing = True
pacman.direction(-2, 0)
agent = TabQLearningAgent()
afficheur = Afficheur(gs)

while playing:
    afficheur.affichage_background()
    #pygame.time.wait(5) #Aucun impact (?)
    if not gs.is_game_over():
        run_step([agent], gs)
    gs.move_all()
    playing, esc = afficheur.affichage_acteurs_et_scores()

print("GAME OVER\nScores : " + str(gs.get_scores()[0]))
if esc: pygame.quit()
