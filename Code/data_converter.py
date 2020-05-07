import csv

class data_converter():
    def __init__(self, fichier_donnees, classe_a_predire):
        self.donnees = []

        print("coucou3")

        with open(fichier_donnees, mode='r', encoding='utf-8-sig') as csv_file:
            print("coucou2")
            csv_reader = csv.DictReader(csv_file)
            print("coucou1")
            for row in csv_reader:
                print("coucouchiant")
                attributs = {}
                print("coucou")
                for a in row:
                    if not a == classe_a_predire:
                        attributs[a] = row[a]
                donnee = [row[classe_a_predire], attributs]

                self.donnees.append(donnee)

