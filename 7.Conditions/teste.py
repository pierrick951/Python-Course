# Structures conditionnelles en Python

# Outils de comparaison
# ======================
# ==      égal à
# !=      différent de (fonctionne aussi avec )
# >       strictement supérieur à
# >=      supérieur ou égal à
# <       strictement inférieur à
# <=      inférieur ou égal à

# Opérateurs logiques
# ====================
# OR      retourne True si au moins l'une des conditions fournies est vraie
# AND     retourne True si toutes les conditions fournies sont vraies

# Comment fonctionnent les structures conditionnelles
# ===================================================
# Utilisation des instructions if, elif et else pour exécuter différents blocs de code en fonction des conditions.

# Exemple de structure conditionnelle
# ====================================
a = 5
if a > 3:
    print('a est plus grand que 3')
elif a < 10:
    print('a est plus petit que 10')
else:
    print("Ce bloc s'exécute si aucune des conditions précédentes n'est vraie")

# Exemple d'utilisation des opérateurs logiques
# =============================================
x = 5
if x < 3 or x > 10:
    print("x est soit inférieur à 3, soit supérieur à 10")

y = 7
if y > 5 and y < 10:
    print("y est plus grand que 5 et plus petit que 10")
