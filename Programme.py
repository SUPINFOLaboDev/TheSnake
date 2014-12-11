import pygame
import sys
import Snake
import Affichage
import Jeu
from pygame.locals import *

pygame.init()          #To test functionnalities there is no need to use pygame
fenetre = pygame.display.set_mode((450, 450))
pygame.display.set_caption('Snake')

serpent = Snake.Snake()
affichage = Affichage.Affichage()
jeu = Jeu.Jeu()

clock = pygame.time.Clock()

speed_x = 0
speed_y = 0
phys_speed = 16

index_physique = 0

pygame.display.flip()

while True:
    fenetre.fill((0, 0, 0))
    clock.tick(60)   # limite le nombre de boucles a 60 par seconde

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                serpent.deplacer_snake("left")

            if event.key == pygame.K_RIGHT:
                serpent.deplacer_snake("right")

            if event.key == pygame.K_UP:
                serpent.deplacer_snake("up")

            if event.key == pygame.K_DOWN:
                serpent.deplacer_snake("down")

    if index_physique > serpent.get_speed():  # la vitesse du serpent est independante de la vitesse de rendu
        serpent.declencher_deplacement_snake()
        # call move python
    else:
        index_physique += 1

    # gerer l'affichage
    affichage.affichage_jeu()

    pygame.display.update()





