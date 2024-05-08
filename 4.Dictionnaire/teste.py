#Les Dictionnaire
#pour en crée un on utilise la syntaxe suivante:

a = {}

#ou
a2 = dict()
#on peut écricre des données dedans grace a des paire(clé/valeurs)
a = {
    "profession":{
    "jour " : "banquier",
    "nuit " : "Hero",
 }
}

#Comment ajouter des données ?

a["nom"] = "wayne"
a["prenom"] = "Bruce"

print(a)


#Récupérer une valeur dans un dictionnaire python 

a.get("name")

#cette methode permet de retourner une valeurs si elle n'est pas presente

a.get("name","nom inconnue")

#et pour verifier la presence d'un element dans un dictionnaire on utilise:

print("nom" in a) #renvoi True


#est pour supprimer on utilise 

del a ["nom"]

#voici une methode pour boucler dans un dictionnaire

for key in a.keys():
    print(key)