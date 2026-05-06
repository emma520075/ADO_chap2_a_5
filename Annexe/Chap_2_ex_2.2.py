"""
/******************************************************************************
 * Nom        : Chap_2_ex_2.2.py
 * Rôle       : Convertir des chiffres romains en entiers et vice-versa, 
 *              et effectuer l'addition de deux nombres romains
 * Auteur     : Emma BARETS
 * Version    : Version finale du 14/12/2025
 * Licence    : Réalisé dans le cadre du cours Architecture des ordinateurs 
 * Dépendances : Aucun module externe requis
 * Usage      : Exécuter le script pour entrer deux nombres romains et obtenir leur somme 
 *              en chiffres romains et en base 10
 ******************************************************************************/
"""

# Exercice 2.2 (Bonus)

def romain_vers_entier(romain):
    """
    Convertit un chiffre romain en entier.
    Gère les majuscules et minuscules.
    Applique les règles classiques :
    - Pas plus de 3 répétitions consécutives pour I, X, C, M
    - V, L, D ne sont jamais répétés
    - Limite de 3999 pour le résultat
    """

    # Dictionnaire contenant la valeur de chaque symbole romain
    valeurs = {
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
        'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000
    }

    # Lettres autorisées à être répétées jusqu’à 3 fois
    repetables = {'I', 'X', 'C', 'M', 'i', 'x', 'c', 'm'}

    compteur = 1   # Compteur pour suivre le nombre de répétitions d'affilées
    total = 0      # Somme finale en base 10
    i = 0          # Index pour parcourir la chaîne 

    # Parcours de chaque symbole du nombre romain
    while i < len(romain):
        lettre = romain[i]

        # Vérification que le caractère est bien un symbole romain
        if lettre not in valeurs:
            print(f"Symbole romain invalide détecté : {lettre}")
            return None

        # Vérification des répétitions d'affilées
        if i > 0 and romain[i] == romain[i-1]:
            compteur += 1
            # Si le symbole peut être répété, on limite à 3
            if lettre in repetables and compteur > 3:
                print(f"Erreur : le symbole {lettre} ne peut pas être répété plus de 3 fois consécutivement.")
                return None
            # Si le symbole ne peut pas être répété du tout (V, L, D)
            elif lettre not in repetables:
                print(f"Erreur : le symbole {lettre} ne peut pas être répété.")
                return None
        else:
            compteur = 1  # Réinitialisation du compteur si symbole différent

        # Vérification que le total ne dépasse pas 3999 
        if total > 3999:
            print("Attention : la numération romaine standard ne supporte pas les nombres > 3999")
            return None

        # Dans le cas où le premier nombre est plus petit que le deuxième 
        if i + 1 < len(romain) and valeurs[lettre] < valeurs[romain[i + 1]]:
            total += valeurs[romain[i + 1]] - valeurs[lettre]
            i += 2  # On saute deux symboles car ils ont été utilisés ensemble
        else:
            total += valeurs[lettre]
            i += 1  # On passe au symbole suivant

    return total  # Renvoie la valeur entière obtenue

#Exercice 2.3

def entier_vers_romain(nombre):
    """
    Convertit un entier en chiffre romain.
    Limite les nombres à 3999 et applique les règles de répétition :
    - I, X, C, M maximum 3 fois consécutives
    - V, L, D jamais répétés
    """
    # Vérification de la limite
    if nombre > 3999:
        print("La numération romaine standard ne supporte pas les nombres > 3999")
        return None

    # Liste ordonnée des symboles romains du plus grand au plus petit
    romains = [
        ('M',1000), ('CM',900), ('D',500), ('CD',400),
        ('C',100), ('XC',90), ('L',50), ('XL',40),
        ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)
    ]

    resultat = ""  # Chaîne qui contiendra le nombre romain final

    # Parcours de chaque couple (c.a.d symbole, valeur)
    for symbole, valeur in romains:
        count = 0  # Compteur pour suivre les répétitions
        # Tant que la valeur actuelle peut être soustraite du nombre
        while nombre >= valeur:
            # Limitation du nombre de répétitions pour chaque symbole
            if symbole in ['I','X','C','M'] and count >= 3:
                break
            elif symbole in ['V','L','D'] and count >= 1:
                break

            # Ajout du symbole et soustraction de sa valeur
            resultat += symbole
            nombre -= valeur
            count += 1

    return resultat  # Renvoie le résultat final

# Lecture des deux nombres romains à additionner
romain1 = input("Entrez le premier nombre romain : ")
romain2 = input("Entrez le second nombre romain : ")

# Conversion en entiers décimaux
entier1 = romain_vers_entier(romain1)
entier2 = romain_vers_entier(romain2)

# Vérification que les conversions ont bien fonctionné
if entier1 is not None and entier2 is not None:
    somme = entier1 + entier2
    print(f"La somme en base 10 est : {somme}")

    # Conversion de la somme en chiffre romain
    romain_resultat = entier_vers_romain(somme)
    if romain_resultat is not None:
        print(f"La somme de {romain1} et {romain2} en chiffres romains est : {romain_resultat}")
    else:
        print("Impossible de convertir ce nombre en chiffres romains standard.")
else:
    print("Erreur lors de la conversion des nombres romains. Impossible de faire l'addition.")
