import pygame
import Jeu
import Snake

class Affichage:

    def __init__(self):
        self.__fenetre = pygame.display.set_mode((450, 450))
        pygame.display.set_caption('Snake')

        self.__resolution_x = 640
        self.__resolution_y = 480
        self.__corps_snake = pygame.image.load("case snake.png")
        print('Affichage cree')

        self.__serpent = Snake.Snake()
        self.__jeu = Jeu.Jeu()

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
        for coord in self.__serpent.get_liste_snake():
            self.__fenetre.blit(self.__corps_snake, (coord[0]*30, coord[1]*30))

        print('snake affiche')

    def affichage_pomme(self):
        print('pomme affiche')

    def affichage_score(self):
        print('score affiche')

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