class NoeudDeDecision:
    """Un noeud dans un arbre de décision. """

    def __init__(self, attribut, donnees, enfants=None):
        """
            :param attribut: l'attribut de partitionnement du noeud (``None`` si\
            le noeud est un noeud terminal).
            :param list donnees: la liste des données qui tombent dans la\
            sous-classification du noeud.
            :param enfants: un dictionnaire associant un fils (sous-noeud) à\
            chaque valeur de l'attribut du noeud (``None`` si le\
            noeud est terminal).
        """

        self.attribut = attribut
        self.donnees = donnees
        self.enfants = enfants

    def terminal(self):
        """ Vérifie si le noeud courant est terminal. """

        return self.enfants is None

    def classe(self):
        """ Si le noeud est terminal, retourne la classe des données qui\
            tombent dans la sous-classification (dans ce cas, toutes les\
            données font partie de la même classe. 
        """

        if self.terminal():
            return self.donnees[0][0]

    def classifie(self, donnee):
        """ Classifie une donnée à l'aide de l'arbre de décision duquel le noeud\
            courant est la racine.

            :param donnee: la donnée à classifier.
            :return: la classe de la donnée selon le noeud de décision courant.
        """

        rep = ''
        if self.terminal():
            rep += 'Alors {}'.format(self.classe().upper())
        else:
            valeur = donnee[self.attribut]
            enfant = self.enfants[valeur]
            if enfant:
                rep += 'Si {} = {}, '.format(self.attribut, valeur.upper())
                rep += enfant.classifie(donnee)
        return rep

    def repr_arbre(self, level=0, compteur_profondeur=[]):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine. 
        """
        rep = ''
        if self.terminal():
            rep += '---'*level
            rep += 'Alors {}\n'.format(self.classe().upper())
            rep += '---'*level
            rep += 'Décision basée sur les données:\n'
            compteur_profondeur.append(level)
            for donnee in self.donnees:
                rep += '---'*level
                rep += str(donnee) + '\n'

        else:
            for valeur, enfant in self.enfants.items():
                if enfant:
                    rep += '---'*level
                    rep += 'Si {} = {}: \n'.format(self.attribut, valeur.upper())
                    rep += enfant.repr_arbre(level+1, compteur_profondeur)[0]

        info = [rep, compteur_profondeur]
        return info

    def __repr__(self):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine. 
        """
        a_afficher = self.repr_arbre(level=0)
        max_profondeur = max(a_afficher[1])
        moy_profondeur = sum(a_afficher[1])/len(a_afficher[1])
        info_arbre = '\n Profondeur max : ' + str(max_profondeur) + '\n Profondeur moyenne : ' + str(moy_profondeur)
        return str(a_afficher[0]) + str(a_afficher[1]) + info_arbre
