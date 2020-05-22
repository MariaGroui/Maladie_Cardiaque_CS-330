from data_converter import data_converter
from moteur_id3_modifie.id3_modifie import ID3

import sys

entree = sys.argv

classe = str(entree[1])
fichier_entrainement = str(entree[2])

donnees = data_converter(fichier_entrainement, classe).donnees

id3 = ID3()
arbre = id3.construit_arbre(donnees)
print(arbre)


fichier_test = str(entree[3])
donnees_test = data_converter(fichier_test, classe).donnees

print("Evaluation de la précision de l'arbre grâce au fichier test : ")

correct = 0
iteration = 0
faux_positif = 0
faux_negatif = 0

for donnee in donnees_test :
    #print('on va classifier une donnée, la vraie classe est ', donnee[0], 'cest parti ')

    classe = arbre.classifie(donnee[1])
    #print('on la classe comme : ', classe[-1])
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
