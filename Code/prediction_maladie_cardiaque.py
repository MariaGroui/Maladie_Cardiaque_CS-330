from moteur_id3.noeud_de_decision import NoeudDeDecision
from resultValues import ResultValues
from moteur_id3.id3 import ID3
import csv
donnees = []
classe = "target"
fichier = 'train_bin.csv'
with open(fichier, mode= 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:

        attributs = {}
        for a in row:
            if not a == classe:
                attributs[a] = row[a]
        donnee = [row[classe], attributs]
        # print(donnee)
        donnees.append(donnee)


resultats = ResultValues(donnees)
a_afficher = resultats.get_results()
print('Arbre de décision :')
print(a_afficher[0])
print()
