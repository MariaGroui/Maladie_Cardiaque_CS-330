from moteur_id3.noeud_de_decision import NoeudDeDecision

class Recherche:

    def __init__(self, conditions_regles_sains = None):
        """
        :param conditions_regles_sains: un tableau contenant pour chaque regle qui predit 'non malade', les conditions correspondantes
        """
        self.conditions_pour_etre_sain = conditions_regles_sains

    def recherche_traitement(self, attributs_patient_malade):
        """
            pour un patient, fait une comparaison avec les regles qui ont une conclusion positive
            note le minimum de changements a faire et les retourne sous forme de dictionnaire
        """
        #print('recherche de traitement pour : ', attributs_patient_malade)
        changements_courant = len(attributs_patient_malade)
        #print('a priori il faut faire ', changements_courant, ' changements, mais voyons ')
        traitement = None
        for conditions in self.conditions_pour_etre_sain:
            #print('nouvelle regles analysée ', conditions)
            changements_a_faire = 0
            for condition in conditions:
                #print('est-ce que ', condition , 'est vrai pour le patient ?')
                #print('frozenset de condition : ', frozenset(condition))
                #print('attributs_patient_malade : ', attributs_patient_malade)
                #if not frozenset(condition).issubset(attributs_patient_malade):
                if not (condition in attributs_patient_malade):
                    #print('et un changement de plus a faire ')
                    changements_a_faire = changements_a_faire + 1
                    #print('pour linstant il faut faire ', changements_a_faire, 'changements')
                if changements_a_faire >= changements_courant:
                    #print('nombre max de changements atteint, on change de regle')
                    break
            if changements_a_faire < changements_courant:
                changements_courant = changements_a_faire
                traitement = conditions.difference(attributs_patient_malade)

        return traitement

