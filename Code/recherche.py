from moteur_id3.noeud_de_decision import NoeudDeDecision
import copy

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
        cur_min_traitement = dict()
        diff_min = len(attributs_patient_malade)
        diff_current = diff_min
        same_rule = True 
                
        for conditions in self.conditions_pour_etre_sain :
            traitement = dict()
            for condition_sain in list(conditions.keys()):
                if same_rule:
                    value_sain = conditions.get(condition_sain)
                    value_malade = attributs_patient_malade.get(condition_sain)
                    if (condition_sain == "sex" and value_sain == value_malade) or (condition_sain == "age" and value_sain == value_malade) or (condition_sain != "sex" and condition_sain != "age") :
                        if not(value_sain == value_malade):
                            traitement[condition_sain] = value_sain
                            diff_current = len(traitement)
                    else:
                        same_rule = False
                        
            if diff_current < diff_min and same_rule:
                diff_min = diff_current
                cur_min_traitement = copy.deepcopy(traitement)
                        
        
        return cur_min_traitement
            
  
         
            
    









