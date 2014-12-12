import Jeu

class Snake:
    
    def __init__(self):
        self.__vitesse_snake = 30  # decrease value to increase speed
        self.__direction = 'left'
        self.__direction_actuel = 'left'
        self.__aggrandir = False

        self.__jeu = Jeu.Jeu()

        self.__liste_snake = []    # deprecated replace with 2 dimension list

        self.__liste_snake.append((7, 7))  # Init a 5 square snake
        self.__liste_snake.append((7, 8))
        self.__liste_snake.append((7, 9))
        self.__liste_snake.append((8, 9))
        self.__liste_snake.append((9, 9))

        print('Snake cree')

    def declencher_deplacement_snake(self):
        self.deplacer_snake()

    def deplacer_snake(self):
        # change the list
        first = True
        old = (0, 0)
        old_x = 0
        old_y = 0

        if self.__direction == 'left' and self.__direction_actuel == 'right':
                self.changer_direction('right')
        if self.__direction == 'right' and self.__direction_actuel == 'left':
                self.changer_direction('left')
        if self.__direction == 'up' and self.__direction_actuel == 'down':
                self.changer_direction('down')
        if self.__direction == 'down' and self.__direction_actuel == 'up':
                self.changer_direction('up')

        for i in range(len(self.__liste_snake)):
            if first:
                old = self.__liste_snake[i]
                if self.__direction == 'left':
                    self.__liste_snake[i] = (self.__liste_snake[i][0] - 1, self.__liste_snake[i][1])
                    self.__direction_actuel = 'left'
                if self.__direction == 'right':
                    self.__liste_snake[i] = (self.__liste_snake[i][0] + 1, self.__liste_snake[i][1])
                    self.__direction_actuel = 'right'
                if self.__direction == 'up':
                    self.__liste_snake[i] = (self.__liste_snake[i][0], self.__liste_snake[i][1] - 1)
                    self.__direction_actuel = 'up'
                if self.__direction == 'down':
                    self.__liste_snake[i] = (self.__liste_snake[i][0], self.__liste_snake[i][1] + 1)
                    self.__direction_actuel = 'down'
                first = False
            else:
                old_x = old[0]
                old_y = old[1]
                old = self.__liste_snake[i]
                self.__liste_snake[i] = (old_x, old_y)
        if self.__aggrandir:
            self.__liste_snake.append((old_x, old_y))
            self.__aggrandir = False
            print('Aggrandi')

        self.__jeu.augmenter_Score(10)
        #print('python moved')

    def agrandir_snake(self):
        self.__aggrandir = True

    def changer_direction(self, direction):

        if direction == 'left' and self.__direction_actuel == 'right':  # Empeche la "marche arriere" su serpent
                direction = 'right'
        if direction == 'right' and self.__direction_actuel == 'left':
                direction = 'left'
        if direction == 'up' and self.__direction_actuel == 'down':
                direction = 'down'
        if direction == 'down' and self.__direction_actuel == 'up':
                direction = 'up'

        self.__direction = direction

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

    def get_jeu(self):
        return self.__jeu
