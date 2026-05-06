"""
/******************************************************************************
 * Nom        : Chap_3_ex_3.14.py
 * Rôle       : Comparer deux nombres décimaux en utilisant la représentation 
 *              en complément à 2 et déterminer le nombre de bits nécessaires
 * Auteur     : Emma BARETS
 * Version    : Version finale du 12/01/2026
 * Licence    : Réalisé dans le cadre du cours Architecture des ordinateurs
 * Dépendances : Aucun module externe requis
 * Usage      : Exécuter le script et saisir deux nombres pour obtenir le plus grand
 ******************************************************************************/
"""

# Saisie des nombres en decimal
a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxieme nombre : "))

# Calcul du nombre minimum de bits pour representer les deux nombres
max_val = max(abs(a), abs(b))
bits = 1
while (1 << (bits - 1)) <= max_val:
    bits += 1

print(f"Nombre de bits utilise : {bits}")

# Fonction pour convertir un nombre en complement a 2 sur 'bits' bits
def to_complement2(n, bits):
    if n < 0:
        n = (1 << bits) + n  # ajouter 2^bits si le nombre est negatif
    return n

# Conversion des nombres en complement a 2
a_bin = to_complement2(a, bits)
b_bin = to_complement2(b, bits)

# Determiner le bit de signe (0 = positif, 1 = negatif)
def bit_signe(n, bits):
    if n >= (1 << (bits - 1)):
        return 1
    else:
        return 0

signe_a = bit_signe(a_bin, bits)
signe_b = bit_signe(b_bin, bits)

# Comparaison selon le signe
if signe_a != signe_b:
    if signe_a == 0:
        print(f"{a} est plus grand que {b}")
    else:
        print(f"{b} est plus grand que {a}")
else:
    # Meme signe : comparer les valeurs en complement a 2
    if a_bin > b_bin:
        print(f"{a} est plus grand que {b}")
    elif a_bin < b_bin:
        print(f"{b} est plus grand que {a}")
    else:
        print(f"{a} et {b} sont egaux")
