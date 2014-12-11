import Programme
import pygame
from pygame.locals import *

class Affichage:

    def __init__(self):
        self.__resolution_x = 640
        self.__resolution_y = 480
        self.__corps_snake = pygame.image.load("case snake.png")
        print('Affichage cree')

    def affichage_jeu(self):
        # affiche le background
        self.affichage_tableau()
        self.affichage_snake()
        self.affichage_pomme()
        self.affichage_score()
        print('jeu affiche')

    def affichage_tableau(self):
        print('tableau affiche')

    def affichage_snake(self):
        liste_test = Programme.serpent.get_liste_snake()
        for coord in liste_test:

        print('snake affiche')

    def affichage_pomme(self):
        print('pomme affiche')

    def affichage_score(self):
        print('score affiche')

    def get_xres(self):
        return self.__resolution_x

    def get_yres(self):
        return self.__resolution_y

    def set_xres(self, valeur):
        self.__resolution_x = valeur

    def set_yres(self, valeur):
        self.__resolution_y = valeur