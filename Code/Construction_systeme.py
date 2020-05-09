from resultValues import ResultValues
from data_converter import data_converter
import sys

if not ( len(sys.argv) == 3 or len(sys.argv) == 4):
    print("Il faut entrer le nom de la classe à prédire ",
          "suivi du nom d'un fichier contenant les données d'apprentissage "
          "et enfin, suivi du nom d'un fichier contenant les données à tester (facultatif) ")
else:

    classe = str(sys.argv[1])
    fichier = str(sys.argv[2])
    donnees = data_converter(fichier, classe).donnees

    #print(donnees)
    resultats = ResultValues(donnees)
    results = resultats.get_results()
    a_afficher = results[0]
    print("Arbre de décision :")
    print(a_afficher)
    print()


    print('regles : ')
    for conditions, c in resultats.regles.items():
        print('Si toutes ces conditins sont valables : ')
        for a, v in conditions:
            print(a, ' = ', v)

        print(' alors la prediction est : ', c)



if len(sys.argv) == 4:

    fichier_test = str(sys.argv[3])
    donnees_test = data_converter(fichier_test, classe).donnees
    arbre_test = results[0]

    correct = 0
    iteration = 0
    faux_positif = 0
    faux_negatif = 0
    for donnee in donnees_test :
        classe = arbre_test.classifie(donnee[1])
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
    

    


