from resultValues import ResultValues
from data_converter import data_converter
from recherche import Recherche
from moteur_id3_modifie.id3_modifie import ID3_modif

import sys

entree = sys.argv

if not (len(entree) == 6):

    print("Il faut entrer le nom de la classe à prédire ",
          "suivi du nom d'un fichier contenant les données d'apprentissage "
          ", suivi du nom d'un fichier contenant les données à tester",
          "Pour avoir un arbre plus précis:",
          "il faut entre le nom d'un fichier contenant les données (continues) d'apprentissage "
          "suivi du nom d'un fichier contenant les données à tester")
else:

    classe = str(entree[1])
    fichier_entrainement = str(entree[2])
    fichier_entrainement_modif = str(entree[4])

    donnees = data_converter(fichier_entrainement, classe).donnees
    donnees_modif = data_converter(fichier_entrainement_modif, classe).donnees

    print("Entrez le numéro d'un exemple de donnée en particulier dont vous voulez l'explication de la prédiction, il y'a ", len(donnees)," données")

    exemple = int(input())
    exemple = donnees[exemple]
    resultats = ResultValues(donnees,donnees_modif)
    results = resultats.get_results()

#Arbre de décision - task 1

    print("Arbre de décision :")
    print(results[0])

#Ensemble de règles generées par l'arbe - task 3

    print("Règles construites grâce à l'arbre : ")
    for conditions, c in results[2].items():
        print('si toutes ces conditions sont valabes : ')
        for a, v in conditions:
            print(a, ' = ', v)

        print('alors la prediction est : ', c)

#La règle declenchée par l'exemple - task 3

    frozen_attributs_exemple = frozenset(exemple[1].items())
    regle_exemple = None

    for conditions, c in results[2].items():
        if conditions.issubset(frozen_attributs_exemple):
            regle_exemple = conditions
        
    print("L'exemple que vous avez choisi : ','\n", exemple,"\n declenche cette regle : " )
    print("Pour : ")
    for a, v in regle_exemple:
        print(a, ' = ', v)
    print("La classe est : ", exemple[0])

#Précisions de l'arbre de décision - task 2

    fichier_test = str(entree[3])
    donnees_test = data_converter(fichier_test, classe).donnees
    arbre_test = results[0]
    print("Evaluation de la précision de l'arbre grâce au fichier test : ")

    correct = 0
    iteration = 0
    faux_positif = 0
    faux_negatif = 0

#Tableau contenant seulement les patients dont la prediction est qu'ils sont malades - task 2

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

#Proposition de traitement pour les données test - task 4

    regles_sains = []
    for conditions, prediction in results[2].items():
        if prediction == '0':
            dict_cond = dict()
            for c in conditions:
                dict_cond[c[0]]=c[1]
            regles_sains.append(dict_cond)

    recherche_diagnostic = Recherche(regles_sains)

    count = 0
    
    for patient in patients_malades:
        attributs_patient = patient[1]
        conseil_de_traitement = recherche_diagnostic.recherche_traitement(attributs_patient)
        
        print('Le patient à guérir a ')

        for a in list(attributs_patient.keys()):
            print(a, ' = ', attributs_patient[a], end=', ')

        print('\npour le guérir il faudrait changer : ')
        for a in list(conseil_de_traitement.keys()):
            print(a, ' = ', conseil_de_traitement[a], end=' ')
        print('\n')

        if len(conseil_de_traitement) <= 2:
            count = count + 1


    print("Nous avons pu conseiller: ", count," patients, avec un ou deux au plus attributs")

#Arbre de décision modifié - task 5

    print("Arbre modifié:")
    print(results[3])

    classe = str(entree[1])
    fichier_test_modif = str(entree[5])
    donnees_test_modif = data_converter(fichier_test_modif, classe).donnees
    arbre_test_modif = results[3]

    print("Evaluation de la précision de l'arbre modifié grâce au fichier test : ")

    correct_modif = 0
    iteration_modif = 0
    faux_positif_modif = 0
    faux_negatif_modif = 0

    for donnee in donnees_test_modif :
        classe = arbre_test_modif.classifie(donnee[1])

        if classe[-1] == donnee[0]:
            correct_modif = correct_modif + 1
        else:
            if classe[-1] == '1':
                faux_positif_modif = faux_positif_modif + 1
            elif classe[-1] == '0':
                faux_negatif_modif = faux_negatif_modif + 1
        iteration_modif = iteration_modif + 1

    print("Le nouveau pourcentage de précision (bonne classification) est:", correct_modif*100/iteration_modif,"%",
          "\nFaux positifs : ", faux_positif_modif, "\nFaux negatifs : ", faux_negatif_modif)


    

    





