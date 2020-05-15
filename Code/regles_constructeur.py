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



    def regle_qui_justifie(self, exemple = None):
        """
        :param exemple: un jeu de donnée
        :return : les faits initiaux (attribut et le valeur correspondante) qui correspondent aux conditions de la règle
        declenchée
        """
        if exemple == None:
        #si aucun exemple n'a ete donné
            print("Aucun exemple à évaluer n'a été donné ")
            return None

        else:
            frozen_attributs_exemple = frozenset(exemple[1].items())
            for conditions, c in self.regles.items():
                if conditions.issubset(frozen_attributs_exemple):
                    return conditions
        #si aucune regle n'a été trouvée
        print('Cet exemple ne declenche aucune règles')
        return None
