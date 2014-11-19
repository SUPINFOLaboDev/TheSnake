import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

pygame.display.flip()

continuer = 1
while continuer:
	continuer = int(input())