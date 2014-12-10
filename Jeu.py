import pygame
import sys
from pygame.locals import *

class Jeu:

    def __init__(self):
        self.__score = 0
        
        '''self.__liste_jeu = []  # Deprecated replace with 2dimension list
        for i in range(255):
            self.__liste_jeu.append(0)'''

        self.__tab_size_x = 0
        self.__tab_size_y = 0
        print('Jeu creer')

    def augmenter_Score(self):
        return 0

    def recup_score(self):
        return 0

    def score(self):
        return 0

    def get_tableau_jeu_indice(self, index):
        return self.__liste_jeu[index]

    def set_tableau_jeu_indice(self, index, valeur):
        self.__liste_jeu[index] = valeur

    def test_collision(self):
        return 0

    def spawn_pomme(self):
        return 0

