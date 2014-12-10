class Snake:
    
    def __init__(self):
        self.__vitesse_snake = 10
        self.__direction = 'none'

        self.__liste_snake = []

        self.__liste_snake.append(112)  # Init a 5 square snake
        self.__liste_snake.append(113)
        self.__liste_snake.append(114)
        self.__liste_snake.append(129)
        self.__liste_snake.append(144)


        self.__taille_snake = len(self.__liste_snake)
        print('Snake cree')


    def declencher_deplacement_snake(self):
        return 0

    def deplacer_snake(self, direction):
        return 0

    def agrandir_snake(self):
        return 0

    def agrandir_liste_snake(self):
        return 0

    def mange_pomme(self):
        return 0





