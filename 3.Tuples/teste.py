#Un Tuple est une liste qui ne peux plus etre modifiée

myTuple = ()

#Pour y ajouter des valeurs

myTuple = (1,"salut","naruto")

#on peut écrire les tuples sans les parenthese mais avec assur de la bonne comprehension du code 

myTuple = 1,"salut","naruto","sasuke"

#quand vous ecrivez un tuples meme avec une seule valeurs oublier pas de mettre la virgule car si non ce n'est plus un tuples

#est pour afficher une valeurs d'un tuple ?

print(myTuple[2]) 

#on peut faire lui faire une affectation multiple

tuples1, tuples2 = 12, 13

print(tuples1)

print(tuples2)

#Il permet également de renvoyer plusieurs valeurs lors d'un appel d'une fonction

def GiveTuple():
    return tuples1,tuples2

GiveTuple()

#On utilisera un tuple pour définir des sortes de constantes qui n'ont donc pas vocation à changer.