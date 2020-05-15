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
        changements_courant = len(attributs_patient_malade)
        regle_a_appliquer = None
        for conditions in self.conditions_pour_etre_sain:
            changements_a_faire = 0
            for condition in conditions:
                if not condition.issubset(attributs_patient_malade):
                    changements_a_faire = changements_a_faire + 1
                if changements_a_faire >= changements_courant: break
            if changements_a_faire < changements_courant:
                changements_courant = changements_a_faire
                regle_a_appliquer = conditions

        return regle_a_appliquer

