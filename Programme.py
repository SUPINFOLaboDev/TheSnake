import pygame
import sys
import Affichage
from pygame.locals import *

pygame.init()          #To test functionnalities there is no need to use pygame

affichage = Affichage.Affichage()

clock = pygame.time.Clock()

speed_x = 0
speed_y = 0
phys_speed = 16

index_physique = 0

pygame.display.flip()

while True:
    affichage.effacer_fenetre()
    clock.tick(60)   # limite le nombre de boucles a 60 par seconde

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                affichage.get_serpent().deplacer_snake("left")

            if event.key == pygame.K_RIGHT:
                affichage.get_serpent().deplacer_snake("right")

            if event.key == pygame.K_UP:
                affichage.get_serpent().deplacer_snake("up")

            if event.key == pygame.K_DOWN:
                affichage.get_serpent().deplacer_snake("down")

    if index_physique > affichage.get_serpent().get_speed():  # la vitesse du serpent est independante de la vitesse de rendu
        affichage.get_serpent().declencher_deplacement_snake()
        # call move python
    else:
        index_physique += 1

    # gerer l'affichage
    affichage.affichage_jeu()

    pygame.display.update()





