import pygame,sys
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Snake')
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
