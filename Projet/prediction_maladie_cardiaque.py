from moteur_id3.noeud_de_decision import NoeudDeDecision
from moteur_id3.id3 import ID3
import csv

import pandas as pd

donnees = pd.read_csv("train_bin.csv")

id3 = ID3()
arbre = id3.construit_arbre(donnees)

print(arbre)
print()

