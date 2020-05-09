from moteur_id3.id3 import ID3
from regles_constructeur import ReglesConstructeur

class ResultValues():

    def __init__(self, donnees = None):

        # Do computations here
        self.donnees = donnees

        # Task 1
        id3 = ID3()
        self.arbre = id3.construit_arbre(donnees)
        # Task 3
        self.faits_initiaux = None
        #self.regles = None
        constructeur_de_regles = ReglesConstructeur(self.arbre)
        self.regles = constructeur_de_regles.Regles()
        # Task 5
        self.arbre_advance = None



    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]



