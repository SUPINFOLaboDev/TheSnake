class Snake:
    
    def __init__(self):
        self.__vitesse_snake = 16
        self.__direction = 'none'
        self.__direction_actuel = 'left'

        self.__liste_snake = []    # deprecated replace with 2 dimension list

        self.__liste_snake.append((7, 7))  # Init a 5 square snake
        self.__liste_snake.append((7, 8))
        self.__liste_snake.append((7, 9))
        self.__liste_snake.append((8, 9))
        self.__liste_snake.append((9, 9))

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

    def get_taille_snake(self):
        return len(self.__liste_snake)

    def get_liste_snake(self):
        return self.__liste_snake


