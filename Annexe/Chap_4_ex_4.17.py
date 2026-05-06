"""
/******************************************************************************
 * Nom        : Chap_4_ex_4.17.py
 * Rôle       : Multiplie deux nombres flottants et affiche le résultat 
 *              normalisé en notation scientifique
 * Auteur     : Emma BARETS
 * Version    : Version final du 03/02/2026
 * Licence    : Réalisé dans le cadre du Architecture des ordinateurs
 * Dépendances : Aucun
 * Usage      : Exécuter le script et saisir deux nombres flottants
 ******************************************************************************/
"""

# Exercice 4.17 - Calcul de e^x avec la formule de Taylor

# Entrer la valeur de x
x = float(input("Entrez la valeur de x : "))

# Entrer le nombre de termes n pour approximer la somme
n = int(input("Entrez le nombre de termes pour l'approximation (plus grand = plus précis) : "))

# Initialisation de la somme avec le premier terme (1)
exp = 1.0

# Boucle pour calculer les termes suivants
fact = 1  # Facteur pour le calcul de la factorielle
puissance = 1  # x^i

for i in range(1, n+1):
    puissance = puissance * x   # Calcul de x^i
    fact = fact * i            # Calcul de i!
    terme = puissance / fact   # Terme de la série
    exp = terme + exp     # Ajouter le terme à la somme

# Affichage du résultat approximatif
print("Approximation de e^", x, "avec", n, "termes : ", exp)