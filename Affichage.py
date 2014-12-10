class Affichage:

    def __init__(self):
        __resolution_x = 640
        __resolution_y = 480
        print('Affichage cree')

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
        print('snake affiche')

    def affichage_pomme(self):
        print('pomme affiche')

    def affichage_score(self):
        print('score affiche')
