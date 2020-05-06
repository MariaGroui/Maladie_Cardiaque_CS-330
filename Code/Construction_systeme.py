from resultValues import ResultValues
from data_converter import data_converter
import sys
if not len(sys.argv) == 3:
    print('il faut entrer le nom de un fichier contenant les données d apprentissage',
          'suivi du nom de la classe a prédire')
else:

    classe = str(sys.argv[2])
    fichier = str(sys.argv[1])
    donnees = data_converter(fichier, classe).donnees

    #print(donnees)

    resultats = ResultValues(donnees)
    a_afficher = resultats.get_results()
    print('Arbre de décision :')
    print(a_afficher[0])
    print()
