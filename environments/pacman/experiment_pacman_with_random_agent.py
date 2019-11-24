from acteurs import *
from agents import RandomAgent
from affichage import Afficheur
from runners import run_step
import pygame


FRAME_RATE = 30
SCREEN_W, SCREEN_H = 232, 272

gs = PacmanArena(SCREEN_W, SCREEN_H)
pacman = PacMan(gs, 108, 184)

playing = True
esc = True
pacman.direction(-2, 0)
agent = RandomAgent()

# Variable temporaire pour activer/désactiver l'affichage pygame
affichage_disabled = True
if not affichage_disabled:
    afficheur = Afficheur(gs)

while playing:
    if not affichage_disabled:
        afficheur.affichage_background()
    #pygame.time.wait(5) #Aucun impact (?)
    if not gs.is_game_over():
        run_step([agent], gs)

    if affichage_disabled:
        for a in gs.actors():
            if not isinstance(a, Wall) and not isinstance(a, Gate):
                x, y, w, h = a.rect()
                xs, ys = a.symbol()

        # Fantomes tués
        for s in reversed(gs.get_scores_sprite()):
            if s[2] == FRAME_RATE * 3:
                gs.scores_sprite.remove(s)
            else:
                s[2] += 1

        # Bonus mangés
        for b in reversed(gs.get_bonus_sprite()):
            if b[2] == FRAME_RATE * 3:
                gs.get_bonus_sprite.remove(b)
            else:
                b[2] += 1

        if gs.nb_life() != 0:
            playing = False
            esc = False
    else: playing, esc = afficheur.affichage_acteurs_et_scores()

print("GAME OVER\nScores : " + str(gs.get_scores()[0]))
if esc: pygame.quit()
