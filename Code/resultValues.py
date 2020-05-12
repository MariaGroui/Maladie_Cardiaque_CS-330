from moteur_id3.id3 import ID3
from regles_constructeur import ReglesConstructeur

class ResultValues():

    def __init__(self, donnees = None, exemple = None):

        # Do computations here
        self.donnees = donnees

        # Task 1
        id3 = ID3()
        self.arbre = id3.construit_arbre(donnees)

        # Task 3
        constructeur_de_regles = ReglesConstructeur(self.arbre)
        self.regles = constructeur_de_regles.regles
        #self.faits_initiaux est toujours un frozenset, il faudra le manipuler comme tel
        self.faits_initiaux = constructeur_de_regles.regle_qui_justifie(exemple)

        # Task 5
        self.arbre_advance = None


    def get_results(self):

        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]



