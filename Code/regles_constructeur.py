from moteur_id3.noeud_de_decision import NoeudDeDecision

class ReglesConstructeur():

    def __init__(self, arbre = None):
        """
        :param arbre: l'arbre a partir duquel les regles sont construites
        """
        self.arbre = arbre
        self.regles = self.Regles()

    def Regles(self):
        """
        construit les regles en parcourant l'arbre de facon similaire a DFS (en profondeur d'abord)
        :return: un dictionnaire associant a chaque ensemble de valeur d'attributs, la classe predite
        """

        return self.chemin(self.arbre)


    def chemin(self, noeud_courant, regles = {}, conditions = {}):

        if noeud_courant.terminal():
            frozen_key = frozenset(conditions.items())
            regles[frozen_key] = noeud_courant.classe()

        else:
            for v, e in noeud_courant.enfants.items():
                conditions[noeud_courant.attribut] = v
                regles = self.chemin(e, regles, conditions)
                del conditions[noeud_courant.attribut]

        return regles


    def Faits_initiaux(self,donnees):

         faits = []
         faits_initiaux = []
         for donnee in donnees:
             faits.append(donnee[1])
         for donnee in faits:
             faits_init = []
             for a in list(donnee.keys()):
                 faits_init.append(donnee[a])
             faits_initiaux.append(faits_init)
             
         

         return faits_initiaux