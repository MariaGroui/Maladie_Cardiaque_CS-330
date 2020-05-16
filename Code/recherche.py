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
        """
        
        #print('recherche de traitement pour : ', attributs_patient_malade)
        changements_courant = len(attributs_patient_malade)
        #print('a priori il faut faire ', changements_courant, ' changements, mais voyons ')
        traitement = None
        for conditions in self.conditions_pour_etre_sain:
            print("malade ",attributs_patient_malade)
            print("conditions: ",conditions)
            #print('nouvelle regles analysée ', conditions)
            changements_a_faire = 0
            for condition in conditions:
                print("condition",condition)
                #print('est-ce que ', condition , 'est vrai pour le patient ?')
                #print('frozenset de condition : ', frozenset(condition))
                #print('attributs_patient_malade : ', attributs_patient_malade)
                #if not frozenset(condition).issubset(attributs_patient_malade):
                if not(condition in attributs_patient_malade):
                    #print('et un changement de plus a faire ')
                    changements_a_faire = changements_a_faire + 1
                    #print('pour linstant il faut faire ', changements_a_faire, 'changements')
                if changements_a_faire >= changements_courant:
                    #print('nombre max de changements atteint, on change de regle')
                    break

            if changements_a_faire < changements_courant :
                changements_courant = changements_a_faire
                traitement = conditions.difference(attributs_patient_malade)
                
        print("traitement",traitement)        
        return traitement
        
        

        """
        
        cur_min_traitement = dict()
        diff_min = len(attributs_patient_malade)
        for conditions in self.conditions_pour_etre_sain :
            traitement = dict()
            for condition_sain in list(conditions.keys()):
                if (condition_sain != "sex" and condition_sain != "age"): 
                    value_sain = conditions.get(condition_sain)
                    value_malade = attributs_patient_malade.get(condition_sain)
                    if not(value_sain == value_malade):
                        traitement[condition_sain] = value_sain
                        diff_current = len(traitement)
            if diff_current < diff_min:
                diff_min = diff_current
                cur_min_traitement = copy.deepcopy(traitement)
                        
        print(cur_min_traitement)
        return cur_min_traitement
            
        """    
        traitement = []
        for conditions_sain in self.conditions_regles_sains:
            for condition_sain in conditions_sain:
                for condition_malade in attributs_patient_malade:
                    if condition_sain[0] == condition_malade[0] and not((condition_sain[0]=="sex") or (condition_sain[0]=="age")) and not(condition_sain[1] == condition_malade[1]):
                        traitement.append(condition.sain)


         return traitement
         """
         
            
    









