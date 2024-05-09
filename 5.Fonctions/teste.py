#Les Fonctions 
#créons une fonction qui return un age 

def age():
    return 28

age() #appel de la fonction 


"""une fonction peut prendre des parametre
cette fonction prend a en argument 
return a + 2"""
 
def age2(a):
    # a est un argument. c'est une valeurs que la fonction attend au momment de l'appel
    return a + 2 

#comme ceci lors de l'appel de la fonction on lui passe la valeurs souhaiter 
print(age2(4)) 


#on peut biensur passer plusieurs parametre a cette fonction
def foo(a,b,c):
    return a + b + c

print(foo(1,2,8)) #comme ceci 


"""⚠️: si une fonction a un argument en parametre, vous devez lui renseigner les données demander,
sans quoi un erreur apparaitra"""



# L'opérateur splat (*) en Python permet de déballer une séquence (liste, tuple, etc.) lors d'un appel de fonction.
# Très utile en Python pour passer des éléments de séquence comme arguments à une fonction.

# Voici comment :
""" 
Nous avons un tuple avec deux valeurs, et en dessous se trouve une fonction avec deux arguments.
Au moment où l'on appelle la fonction, on passe le tuple en argument à l'aide de l'opérateur splat (*) qui étend les valeurs.

En gros, le a et le b prennent 1 et 2 comme valeurs.
"""

mon_tuple = (1, 2)

def ma_fonction(a, b):
    """Cette fonction retourne la somme de ses deux arguments."""
    return a + b

# Affiche la somme des éléments du tuple
print(ma_fonction(*mon_tuple))

#le splat a ** est utiliser pour les dictionnaire 

mon_dictionnaire = {
    'prenom':'Jean',
    'nom': 'Bonbeurre'
}

def fonction_duo_splate(prenom,nom):
    
    print('voici mon Prenom :', prenom)
    print('voici mon Nom :', nom)


#Appel de la fonction en utilisant l'opérateur double-splat

fonction_duo_splate(**mon_dictionnaire)
