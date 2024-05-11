# Les boucles en Python

# Il existe deux types de boucles en Python : For et While.

# La boucle For permet de parcourir un élément, comme une chaîne de caractères ou une liste.

mot = 'python'

for lettre in mot:
    print(lettre)

# Renvoie :
# p
# y
# t
# h
# o
# n

# On peut utiliser Range.

for i in range(0, 251):
    print(i)

# Cela va boucler jusqu'au nombre 250. Notez que le 0 est le premier chiffre.

# Il existe une fonctionnalité appelée "Break" qui permet de sortir de la boucle quand une certaine condition est remplie.

liste = [1, 2, 50, 61, 84, 15, 23]

for i in liste:
    if i > 62:
        print("Les nombres au-dessus de 62 ne sont pas affichés.")
        break
    print(i)

# Renvoie :
# 1
# 2
# 50
# 61
# Les nombres au-dessus de 62 ne sont pas affichés.

# Maintenant, voyons la boucle While.

# C'est une boucle infinie qui s'exécute tant que la condition est vraie.
# En anglais, "while" signifie "tant que".

i = 0
while i < 10:
    print('hello from the loop')
    i += 1

# ⚠️ Attention aux boucles infinies.

# Exemple de boucle infinie :
# Boucle infinie
# while True:
#     print("Cette boucle est infinie!")


# Attention à ne pas oublier d'incrémenter, sinon la boucle bouclera indéfiniment.

# Pour décrémenter, on écrit ceci : i -= 1 ou i = i - 1.
