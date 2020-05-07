from resultValues import ResultValues
from data_converter import data_converter
import sys

if not ( len(sys.argv) == 3 or len(sys.argv) == 4):
    print("Il faut entrer le nom d'un fichier contenant les données d'apprentissage",
          "suivi du nom d'un fichier contenant les dosnnées à tester (facultatif)"
          "et enfin, suivi du nom de la classe à prédire")
else:

    classe = str(sys.argv[3])
    fichier = str(sys.argv[1])
    donnees = data_converter(fichier, classe).donnees

    #print(donnees)
    resultats = ResultValues(donnees)
    results = resultats.get_results()
    a_afficher = results[0]
    print("Arbre de décision :")
    print(a_afficher)
    print()

if len(sys.argv) == 4:

    fichier_test = str(sys.argv[2])
    donnees_test = data_converter(fichier_test, classe).donnees_test
    arbre_test = results[0]

    correct = 0
    iteration = 0

    for donnee in donnees_test :
        classe = arbre_test.classifie(donnees_test)
        if classe == donnee[0] :
            correct = correct + 1

        iteration = iteration + 1

    print("Le pourcentage de bonne classification est: ")
    print( correct*100/iteration ) 
        
    

    


