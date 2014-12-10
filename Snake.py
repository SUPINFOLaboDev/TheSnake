class Snake:
    
    def __init__(self):
        self.__vitesse_snake = 10
        self.__taille_snake = 5
        self.__direction = 'none'
        self.__liste_snake = []
        for i in range(255):
            self.__liste_snake.append(0)

        self.__liste_snake[112] = 1  # Init a 5 square snake
        self.__liste_snake[113] = 1
        self.__liste_snake[114] = 1
        self.__liste_snake[129] = 1
        self.__liste_snake[144] = 1

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





