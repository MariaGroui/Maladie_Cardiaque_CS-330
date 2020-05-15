from resultValues import ResultValues
from data_converter import data_converter
from recherche import Recherche
import sys

entree = sys.argv

if not (len(entree) == 3 or len(entree) == 4):

    print("Il faut sentrer le nom de la classe à prédire ",
          "suivi du nom d'un fichier contenant les données d'apprentissage "
          "et enfin, suivi du nom d'un fichier contenant les données à tester (facultatif) ")
else:

    classe = str(entree[1])
    fichier_entrainement = str(entree[2])
    donnees = data_converter(fichier_entrainement, classe).donnees

    print("Entrez le numéro d'un exemple de donnée en particulier dont vous voulez l'explication de la prédiction, il y'a ", len(donnees)," données")
    exemple = int(input())
    exemple = donnees[exemple]
    #exemple = None
    resultats = ResultValues(donnees, exemple)
    results = resultats.get_results()

#Arbre de décision 

    print("Arbre de décision :")
    print(results[0])
    #print()

#Ensemble de règles generées par l'arbe

    print('regles construites grace a larbre : ')
    for conditions, c in results[2].items():
        print('si toutes ces conditions sont valabes : ')
        for a, v in conditions:
            print(a, ' = ', v)

        print('alors la prediction est : ', c)


"""
#La règle declenchée par l'exemple

    if not results[1] == None:
        print("L'exemple que vous avez choisi : ','\n", exemple,"\n declenche cette regle : " )
        print("Pour : ")
        for a, v in results[1]:
            print(a, ' = ', v)

        print("La classe est : ", exemple[0])
"""
#Précisions de l'arbre de décision

if len(entree) == 4:
    fichier_test = str(entree[3])
    donnees_test = data_converter(fichier_test, classe).donnees
    arbre_test = results[0]
    print("Evaluation de la précision de l'arbre grâce au fichier test : ")

    correct = 0
    iteration = 0
    faux_positif = 0
    faux_negatif = 0

    #tableau contenant seulement les patients dont la prediction est qu'ils sont malades
    patients_malades = []

    for donnee in donnees_test :
        classe = arbre_test.classifie(donnee[1])
        if classe[-1] == '1':
            patients_malades.append(donnee)
        if classe[-1] == donnee[0]:
            correct = correct + 1

        else:
            if classe[-1] == '1':
                faux_positif = faux_positif + 1
            elif classe[-1] == '0':
                faux_negatif = faux_negatif + 1
        iteration = iteration + 1

    print("Le pourcentage de précision (bonne classification) est:",correct*100/iteration,"%",
          "\nFaux positifs : ", faux_positif, "\nFaux negatifs : ", faux_negatif)
    

#tache 4, proposition de traitement pour les données test
    regles_sains = []
    for conditions, prediction in results[2].items():
        if prediction == '1':
            regles_sains.append(conditions)
    recherche_diagnostic = Recherche(regles_sains)
    for attributs_patient in patients_malades:
        conseil_de_traitement = recherche_diagnostic.recherche_traitement(frozenset(attributs_patient[1].items()))
        print('pour guerir il faudrait : ')

