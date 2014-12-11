import pygame
import sys
from pygame.locals import *

class Jeu:

    def __init__(self):
        self.__score = 0
        self.__liste_jeu = [[None for x in range(15)] for y in range(15)]

        self.__tab_size_x = 0
        self.__tab_size_y = 0
        print('Jeu creer')

    def augmenter_Score(self):
        return 0

    def recup_score(self):
        return 0

    def score(self):
        return 0

    def get_tableau_jeu_indice(self, index_x, index_y):
        return self.__liste_jeu[index_x][index_y]

    def set_tableau_jeu_indice(self, index_x, index_y, valeur):
        self.__liste_jeu[index_x][index_y] = valeur

    def test_collision(self):
        return 0

    def spawn_pomme(self):
        return 0

