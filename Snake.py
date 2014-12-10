class Snake:
    
    def __init__(self):
        self.__vitesse_snake = 16
        self.__direction = 'none'

        '''self.__liste_snake = []    # deprecated replace with 2 dimension list

        self.__liste_snake.append(112)  # Init a 5 square snake
        self.__liste_snake.append(113)
        self.__liste_snake.append(114)
        self.__liste_snake.append(129)
        self.__liste_snake.append(144)'''


        self.__taille_snake = 0
        print('Snake cree')


    def declencher_deplacement_snake(self):
        self.deplacer_snake(self.__direction)

    def deplacer_snake(self, direction):
        # change the list
        print('python moved')

    def agrandir_snake(self):
        return 0

    def agrandir_liste_snake(self):
        return 0

    def mange_pomme(self):
        return 0

    def get_speed(self):
        return self.__vitesse_snake

    def set_speed(self, value):
        self.__vitesse_snake = value




