"""
/******************************************************************************
 * Nom        : Chap_4_ex_4.13.py
 * Rôle       : Multiplie deux nombres flottants et affiche le résultat 
 *              normalisé en notation scientifique
 * Auteur     : Emma BARETS
 * Version    : Version finale du 02/02/2026
 * Licence    : Réalisé dans le cadre du cours Architecture des ordinateurs
 * Dépendances : Aucun
 * Usage      : Exécuter le script et saisir deux nombres flottants
 ******************************************************************************/
"""

# Exercice 4.13 

# Donner deux nombres flottants a et b
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# Multiplier les deux nombres
resultat = a * b

# Initialiser l'exposant pour après
expo = 0

# Normaliser pour avoir exactement un chiffre à gauche de la virgule
if resultat != 0:
    while abs(resultat) >= 10:
        resultat = resultat/10
        expo = expo + 1
    while abs(resultat) < 1:
        resultat = resultat * 10
        expo = expo - 1

# Affichage du résultat normalisé 
print("Résultat normalisé :", resultat)
print("Exposant :", expo)
print("Résultat en notation scientifique :", str(resultat) + " x 10^" + str(expo))


