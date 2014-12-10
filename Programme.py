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



serpent = Snake.Snake()
affichage = Affichage.Affichage()
jeu = Jeu.Jeu()
