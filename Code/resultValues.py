from moteur_id3.id3 import ID3
from moteur_id3_modifie.id3_modifie import ID3_modif
from regles_constructeur import ReglesConstructeur

class ResultValues():

    def __init__(self, donnees = None, donnees_modif = None):

        # Do computations here
        self.donnees = donnees
        self.donnees_modif = donnees_modif

        # Task 1
        id3 = ID3()
        self.arbre = id3.construit_arbre(donnees)

        # Task 3
        constructeur_de_regles = ReglesConstructeur(self.arbre)
        self.regles = constructeur_de_regles.regles
        self.faits_initiaux = constructeur_de_regles.Faits_initiaux(self.donnees)

        # Task 5
        id3_modif = ID3_modif()
        self.arbre_advance = id3_modif.construit_arbre(donnees_modif)


    def get_results(self):

        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]
