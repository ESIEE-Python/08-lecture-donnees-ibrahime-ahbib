"""
Ce module permet de lire des données à partir d'un fichier CSV et d'effectuer 
des opérations simples sur les listes d'entiers extraites.
"""

import os

FILENAME = "listes.csv"


#### Fonctions secondaires

def read_data(filename):
    """Retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 liste par ligne)
    """
    l = []

    # On spécifie l'encodage pour éviter des erreurs potentielles
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # On split à ; et on convertit en int chaque entier splité
            l.append([int(i) for i in line.strip().split(";")])

    return l


def get_list_k(data, k):
    """Retourne la k-ième liste de data si elle existe.

    Args:
        data (list): une liste de listes d'entiers
        k (int): indice de la liste à récupérer

    Returns:
        list: la k-ième liste ou une liste vide si k dépasse la longueur de data
    """
    l = []

    if k < len(data):
        l = data[k]

    return l


def get_first(l):
    """Retourne le premier élément de la liste l."""
    return l[0]


def get_last(l):
    """Retourne le dernier élément de la liste l."""
    return l[-1]


def get_max(l):
    """Retourne la valeur maximale de la liste l."""    
    # Utilisation de max pour simplifier le code
    return max(l)


def get_min(l):
    """Retourne la valeur minimale de la liste l."""
    # Utilisation de min pour simplifier le code
    return min(l)


def get_sum(l):
    """Retourne la somme des éléments de la liste l."""
    return sum(l)


#### Fonction principale

def main():
    """Fonction principale qui affiche les données du fichier et une liste spécifique."""

    if os.path.exists(FILENAME):
        data = read_data(FILENAME)
        for i, l in enumerate(data):
            print(i, l)

        k = 37
        print(k, get_list_k(data, k))
    else:
        print(f"Le fichier {FILENAME} n'existe pas.")


if __name__ == "__main__":
    main()
