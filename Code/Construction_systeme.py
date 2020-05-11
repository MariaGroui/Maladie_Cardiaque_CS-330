from resultValues import ResultValues
from data_converter import data_converter
import sys

entree = sys.argv

if not (len(entree) == 3 or len(entree) == 4):

    print("Il faut entrer le nom de la classe à prédire ",
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

    """
#Ensemble de regles generées par l'arbe
    print('regles construites grace a larbre : ')
    for conditions, c in results[2].items():
        print('si toutes ces conditions sont valabes : ')
        for a, v in conditions:
            print(a, ' = ', v)

        print('alors la prediction est : ', c)
    """
#la regle declenchée par l'exemple
    if not results[1] == None:
        print('lexemple que vous avez choisi : ','\n', exemple,'\n declenche cette regle : ' )
        print('Pour : ')
        for a, v in results[1]:
            print(a, ' = ', v)

        print('la classe est : ', exemple[0])

#Précisions de l'arbre de décision

if len(entree) == 4:
    fichier_test = str(entree[3])
    donnees_test = data_converter(fichier_test, classe).donnees
    arbre_test = results[0]
    print('Evaluation de la precision de larbre grace au fichier test : ')

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
    


