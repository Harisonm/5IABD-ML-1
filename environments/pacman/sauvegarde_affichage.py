import pygame
from acteurs import *


class Afficheur():

    def __init__(self, map: PacmanArena):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(map.size())
        self.background = pygame.image.load('resources/pacman_background.png')
        self.sprites = pygame.image.load('resources/pacman_sprites.png')
        self.map = map

    def affichage_background(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

    def affichage_acteurs_et_scores(self):
        playing = True
        esc = True
        # Afficher les personnages
        for a in self.map.actors():
            if not isinstance(a, Wall) and not isinstance(a, Gate):
                x, y, w, h = a.rect()
                xs, ys = a.symbol()
                self.screen.blit(self.sprites, (x, y), area = (xs, ys, w, h))

        # Afficher les scores
        font = pygame.font.SysFont('Courier', 14)
        msg = font.render(str(int(self.map.get_scores()[0])), True, (255, 255, 255))
        self.screen.blit(msg, (6, 254))

        # Fantomes tués
        for s in reversed(self.map.get_scores_sprite()):
            self.screen.blit(self.sprites, s[0], area = (s[1]*16, 128, 16, 16))
            if s[2] == FRAME_RATE*3: self.map.scores_sprite.remove(s)
            else: s[2] += 1

        # Bonus mangés
        for b in reversed(self.map.get_bonus_sprite()):
            self.screen.blit(self.sprites, b[0], area = (b[1]*16, 144, 16, 16))
            if b[2] == FRAME_RATE*3: self.map.get_bonus_sprite.remove(b)
            else: b[2] += 1

        # Afficher les vies
        for l in range(self.map.getLifes()):
            self.screen.blit(self.sprites, (210 - l*16, 254), area = (128, 16, 16, 16))

        # READY ?
        if self.map.get_status() == -1 and self.map.nb_life() == 0:
            msg = font.render("READY!", True, (255, 255, 0))
            self.screen.blit(msg, (92, 136))

        # Est-ce la fin de la partie ?
        if self.map.nb_life() != 0:
            if self.map.nb_life() == 1:
                msg = font.render("YOU WIN", True, (255, 255, 0))
                screen.blit(msg, (88, 136))
            elif self.map.nb_life() == 2:
                msg = font.render("GAME OVER", True, (255, 0, 0))
                self.screen.blit(msg, (80, 136))
            #self.map.sound(3).stop()
            playing = False
            esc = False
        pygame.display.flip()
        self.clock.tick(FRAME_RATE)
        return playing, esc