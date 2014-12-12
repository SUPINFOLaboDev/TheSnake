import pygame
import Snake

class Affichage:

    def __init__(self):
        self.__fenetre = pygame.display.set_mode((450, 470))
        pygame.display.set_caption('Snake')

        self.__resolution_x = 450
        self.__resolution_y = 470
        self.__corps_snake = pygame.image.load("case snake.png").convert()
        self.__background = pygame.image.load("background.png").convert()

        self.__serpent = Snake.Snake()

        self.__police = pygame.font.SysFont("police/verdana.ttf", 30)
        self.__affichage__score = self.__police.render(str(self.__serpent.get_jeu().get_score()), 1, (0, 0, 0))


    def affichage_jeu(self):
        self.affichage_tableau()
        self.affichage_snake()
        self.affichage_pomme()
        self.affichage_score()

    def affichage_tableau(self):
        self.__fenetre.blit(self.__background, (0, 0))

    def affichage_snake(self):
        for coord in self.__serpent.get_liste_snake():
            self.__fenetre.blit(self.__corps_snake, (coord[0]*30, coord[1]*30))


    def affichage_pomme(self):
        return 0

    def affichage_score(self):
        self.__affichage__score = self.__police.render(str(self.__serpent.get_jeu().get_score()), 1, (132, 132, 132))
        self.__fenetre.blit(self.__affichage__score, (0, 450))
        print('test' + str(self.__serpent.get_jeu().get_score()))

    def effacer_fenetre(self):
        self.__fenetre.fill((0, 0, 0))

    def get_xres(self):
        return self.__resolution_x

    def get_yres(self):
        return self.__resolution_y

    def set_xres(self, valeur):
        self.__resolution_x = valeur

    def set_yres(self, valeur):
        self.__resolution_y = valeur

    def get_serpent(self):
        return self.__serpent