from moteur_id3.id3 import ID3
class ResultValues():

    def __init__(self, donnees = None):

        # Do computations here
        self.donnees = donnees

        # Task 1
        id3 = ID3()
        self.arbre = id3.construit_arbre(donnees)
        # Task 3
        self.faits_initiaux = None
        self.regles = None
        # Task 5
        self.arbre_advance = None



    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]

    def get_profondeur(self):
        """ parcourt l'arbre pour etidier sa profondeur
        :return: un vecteur contenant la profondeur maximale et la profondeur \
        maximale et la profondeur minimale
        """


