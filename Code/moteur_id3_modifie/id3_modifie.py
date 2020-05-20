from math import log
from .noeud_de_decision_modifie import NoeudDeDecision

class ID3:
    """ Algorithme ID3. 

        This is an updated version from the one in the book (Intelligence Artificielle par la pratique).
        Specifically, in construit_arbre_recur(), if donnees == [] (line 70), it returns a terminal node with the predominant class of the dataset -- as computed in construit_arbre() -- instead of returning None.
        Moreover, the predominant class is also passed as a parameter to NoeudDeDecision().

        difference par rapport a la version non modifiee: les valeurs des attributs sont continues, un noeud divise avec un attribut et une valeur particuliere

    """
    
    def construit_arbre(self, donnees):
        """ Construit un arbre de décision à partir des données d'apprentissage.

            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """
        
        # Nous devons extraire les domaines de valeur des 
        # attributs, puisqu'ils sont nécessaires pour 
        # construire l'arbre.
        attributs = {}
        for donnee in donnees:
            for attribut, valeur in donnee[1].items():
                valeurs = attributs.get(attribut)
                if valeurs is None:
                    valeurs = set()
                    attributs[attribut] = valeurs
                valeurs.add(float(valeur))
        print(attributs)
        #attributs contient pour chaque attribut, toutes les valeurs qui apparaissent
        # Find the predominant class
        classes = set([row[0] for row in donnees])
        # print(classes)
        predominant_class_counter = -1
        for c in classes:
            # print([row[0] for row in donnees].count(c))
            if [row[0] for row in donnees].count(c) >= predominant_class_counter:
                predominant_class_counter = [row[0] for row in donnees].count(c)
                predominant_class = c
        # print(predominant_class)
            
        arbre = self.construit_arbre_recur(donnees, attributs, predominant_class)

        return arbre

    def construit_arbre_recur(self, donnees, attributs, predominant_class):
        """ Construit rédurcivement un arbre de décision à partir 
            des données d'apprentissage et d'un dictionnaire liant
            les attributs à la liste de leurs valeurs possibles.

            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :param attributs: un dictionnaire qui associe chaque\
            attribut A à son domaine de valeurs a_j.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """
        
        def classe_unique(donnees):
            """ Vérifie que toutes les données appartiennent à la même classe. """
            
            if len(donnees) == 0:
                return True 
            premiere_classe = donnees[0][0]
            for donnee in donnees:
                if donnee[0] != premiere_classe:
                    return False 
            return True

        if donnees == []:
            return NoeudDeDecision(None, [str(predominant_class), dict()], str(predominant_class))

        # Si toutes les données restantes font partie de la même classe,
        # on peut retourner un noeud terminal.         
        elif classe_unique(donnees):
            return NoeudDeDecision(None, donnees, str(predominant_class))
            
        else:
            # Sélectionne l'attribut qui réduit au maximum l'entropie.
            h_C_As_attribs = [[(self.h_C_A(donnees,attribut, float(valeur)), attribut, float(valeur))
                               for valeur in range(int(min(attributs[attribut])), int(max(attributs[attribut])))]
                              for attribut in attributs]

                #min(h_C_As_attribs, key=lambda h_a_v: h_a_v[0])
            min_h = h_C_As_attribs[0][0]
            for a in h_C_As_attribs:
                for v in a:
                    if v[0] < min_h[0]: min_h = v
            attribut = min_h[1]
            valeur_de_partition = min_h[2]

            partitions = self.partitionne(donnees, attribut, valeur_de_partition)
            
            enfants = {}
            valeurs_sup=[]
            valeurs_inf=[]
            for valeur in attributs[attribut]:
                if valeur >= valeur_de_partition: valeurs_sup.append(valeur)
                elif valeur < valeur_de_partition: valeurs_inf.append(valeur)
            for sup_ou_egal, partition in partitions.items():
                if sup_ou_egal:
                    attributs_adapte = attributs.copy()
                    attributs_adapte[attribut] = valeurs_sup
                    enfants[tuple(valeurs_sup)] = self.construit_arbre_recur(partition,
                                                             attributs_adapte,
                                                             predominant_class)
                elif not sup_ou_egal:
                    attributs_adapte = attributs.copy()
                    attributs_adapte[attribut] = valeurs_inf
                    enfants[tuple(valeurs_inf)] = self.construit_arbre_recur(partition,
                                                                      attributs_adapte,
                                                                      predominant_class)

            return NoeudDeDecision(attribut, donnees, str(predominant_class), enfants)

    def partitionne(self, donnees, attribut, valeur_de_partition):
        """ Partitionne les données sur les valeurs a_j de l'attribut A.

            :param list donnees: les données à partitioner.
            :param attribut: l'attribut A de partitionnement.
            :param list valeurs: les valeurs a_j de l'attribut A.
            :return: un dictionnaire qui associe à chaque valeur a_j de\
            l'attribut A une liste l_j contenant les données pour lesquelles A\
            vaut a_j.
        """
        #ici il ne faut plus que la partition se fasse selon toutes les valeurs mais seulement en deux
        #selon une limite qui reduit au max l'entropie
        partitions = {sup_ou_egal: [] for sup_ou_egal in (True, False)}
        
        for donnee in donnees:
            if float(donnee[1][attribut]) >= valeur_de_partition:
                partitions[True].append(donnee)
            else:
                partitions[False].append(donnee)
            #partitions[donnee[1][attribut] >= valeur_de_partition].append(donnee)
        return partitions

    def p_a_sup_val(self, donnees, attribut, valeur_de_partition):
        """ p(a >= valeur_de_partition) - la probabilité que la valeur de l'attribut A soit >= a une valeur.

            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur_de_partition: la valeur de A seln laquelle on divise
            :return: p(a >= valeur_de_partition)
        """
        # Nombre de données.
        nombre_donnees = len(donnees)
        
        # Permet d'éviter les divisions par 0.
        if nombre_donnees == 0:
            return 0.0
        
        # Nombre d'occurrences de a_j >= valeur_de_partition parmi les données.
        nombre_aj = 0
        for donnee in donnees:
            if float(donnee[1][attribut]) >= valeur_de_partition:
                nombre_aj += 1

        # p(a_j) = nombre d'occurrences de la valeur a_j parmi les données / 
        #          nombre de données.
        return nombre_aj / nombre_donnees

    def p_ci_aj(self, donnees, attribut, valeur_de_partition, classe, sup_ou_egal = True):
        """ p(c_i|a_j) - la probabilité conditionnelle que la classe C soit c_i\
            étant donné que l'attribut A >= ou < que valeur_de_partition.

            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur: la valeur a_j de l'attribut A.
            :param classe: la valeur c_i de la classe C.
            :return: p(c_i | a_j)
        """
        # Nombre d'occurrences de la valeur a_j parmi les données.
        if sup_ou_egal:
            donnees_aj = [donnee for donnee in donnees if float(donnee[1][attribut]) >= valeur_de_partition]
        else:
            donnees_aj = [donnee for donnee in donnees if float(donnee[1][attribut]) < valeur_de_partition]
        nombre_aj = len(donnees_aj)
        
        # Permet d'éviter les divisions par 0.
        if nombre_aj == 0:
            return 0
        
        # Nombre d'occurrences de la classe c_i parmi les données pour lesquelles 
        # A vaut >= ou < valeur_de_partition.
        donnees_ci = [donnee for donnee in donnees_aj if donnee[0] == classe]
        nombre_ci = len(donnees_ci)

        # p(c_i|a_j) = nombre d'occurrences de la classe c_i parmi les données 
        #              pour lesquelles A vaut a_j /
        #              nombre d'occurrences de la valeur a_j parmi les données.
        return nombre_ci / nombre_aj

    def h_C_aj(self, donnees, attribut, valeur_de_partition, sup_ou_egal = True):
        """ H(C|a >) - l'entropie de la classe parmi les données pour lesquelles\
            l'attribut A vaut a_j.

            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur_de_partition: la valeur de partition pour l'attribut A.
            :param sup_ou_egal: dit si on cherche H(C|a>=valeur_de_partition) ou H(C|a<valeur_de_partition)
            :return: H(C|a_j)
        """
        # Les classes attestées dans les exemples.
        classes = list(set([donnee[0] for donnee in donnees]))
        
        # Calcule p(c_i|a_j) pour chaque classe c_i.

        p_ci_ajs = [self.p_ci_aj(donnees, attribut, valeur_de_partition, classe, sup_ou_egal)
                    for classe in classes]

        # Si p vaut 0 -> plog(p) vaut 0.
        return -sum([p_ci_aj * log(p_ci_aj, 2.0) 
                    for p_ci_aj in p_ci_ajs 
                    if p_ci_aj != 0])

    def h_C_A(self, donnees, attribut, valeur_de_partition):
        """ H(C|A) - l'entropie de la classe après avoir choisi de partitionner\
            les données suivant les valeurs de l'attribut A.
            
            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param list valeur_de_partition: la valeur de l'attribut A selon laquelle on divise.
            :return: H(C|A)
        """
        # calcule p(a >= valeur_de_partition) et p(a < valeur_de_partition). ou a est la valeur de l'attribut A
        p_a_sup = self.p_a_sup_val(donnees, attribut,valeur_de_partition)
        p_a_inf = 1-p_a_sup
        p_as = [p_a_sup, p_a_inf]

        # Calcule H(C|a>=valeur_de_partition) et H(C|a<valeur_de_partition)
        h_C_a_sup = self.h_C_aj(donnees, attribut, valeur_de_partition, sup_ou_egal=True)
        h_C_a_inf = self.h_C_aj(donnees, attribut, valeur_de_partition, sup_ou_egal=False)
        h_c_as = [h_C_a_sup, h_C_a_inf]


        return sum([p_a * h_c_a for p_a, h_c_a in zip(p_as, h_c_as)])