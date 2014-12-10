import pygame
import sys
import Snake
import Affichage
import Jeu
from pygame.locals import *

"""pygame.init()          //To test functionnalities there is no need to use pygame
fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Snake')
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()"""



class Programme:  # main class allow to call every other class created

    def __init__(self):
        self.__serpent = Snake.Snake()
        self.__affichage = Affichage.Affichage()
        self.__jeu = Jeu.Jeu()

    def getSerpent(self):
        return self.__serpent

    def getAffichage(self):
        return self.__affichage

    def getJeu(self):
        return self.__affichage

test = Programme()
test.getAffichage().affichage_tableau()