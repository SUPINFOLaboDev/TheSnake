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

    def augmenter_Score(self, valeur):
        self.__score += valeur

    def get_score(self):
        return self.__score

    def set_score(self, valeur):
        self.__score = valeur

    def get_tableau_jeu_indice(self, index_x, index_y):
        return self.__liste_jeu[index_x][index_y]

    def set_tableau_jeu_indice(self, index_x, index_y, valeur):
        self.__liste_jeu[index_x][index_y] = valeur

    def test_collision(self, liste):
        if 14 < liste[0][0] or 0 > liste[0][0] or 14 < liste[0][1] or 0 > liste[0][1]:
            return True

        for i in range(1, len(liste)):
            if liste[0] == liste[i]:
                return True

    def spawn_pomme(self):
        return 0

