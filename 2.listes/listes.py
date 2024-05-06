#découvrons les liste

#Voici comment on crée une liste
liste = []

#Maitenant voyons comment on peut y ajouter du contenus 

liste = [1,2,3]



#Est comment on ajoute du contenu quand on finit de crée la liste ?

liste.append(4)


#Oui mais si je veux afficher un éléments de la liste ? 

print(liste[2]) #On le print avec le nom de la liste est sont index dans le tableau

#tips le premier  élément d'une liste a toujours l'index 0



#----------------------------------------------------
#Pour supprimer une entrée du tableau avec  son index

del liste[2]
print(liste) #le chiffre 3 est supprimer 

#est maintenant voyons comment supprimer un element du tableau avec ça valeurs

liste.remove(1)
print(liste) #le 1 est supprimer

#compter la longeur de la liste 

print(len(liste)) # affiche 2

#D'accord mais si on ne connait pas sont index ? 
liste.index(2)



#Manipuler une liste ?

liste [-1] #renvoie la derniere occurence de la liste 
# liste [-4] #renvoie les 4 occurence de la liste

liste [:] #affiche toute les occurences

#Et pour afficher une parti souhaiter dans la liste ?

liste [0:2] #renvoie seulement les index de 0 a 2

#est voici comment on vide la liste 

liste[:] = []


#-------------------------------
#Boucler sur une liste 

listeFruits = ['🍇','🍉','🍈','🍌','🥝']

#on utilise une boucle For

for fruit in listeFruits:
    print(fruit)


#est pour recupere l'index on utilise la fontion enumerate

for fruitIndex in enumerate(listeFruits):
    print(fruitIndex)

# return
# (0, '🍇')
# (1, '🍉')
# (2, '🍈')
# (3, '🍌')
# (4, '🥝')


# Maitenant on va découvrire la copie d'une liste

#voici une liste
sport = ['🥊','🏈','🏀','⚽']

#on est tenter de faire ceci 

sport2 = sport

#ok ça fonctionne mais voyons de plus pres ce genre de copy 
# c'est ce qu'on appelle une copy superficiel
#autrement dit si on change un element dans sport2 sport cera affecter de changement

sport2.append('⚾')
print(sport) #return ['🥊', '🏈', '🏀', '⚽', '⚾']

#POURQUOI ??
#pas de panique je t'explique
#les liste et varible sont stocker dans une memoire 
#est en fesant sport2 = sport
#on pointe simplement l'endroit ou est stocker sport
#donc c'est une reference est pas une copy 
#il  partage le meme emplacement dans la memoire 

#mais alors comment faire une copie  qui pointe vers  son propre emplacement ? 

#OK on va voir ça
# c'est partie pour faire une Deepcopy

import copy #on import le module copy
sport2 = copy.deepcopy(sport)
sport2.append('🏐')
print(sport) #['🥊', '🏈', '🏀', '⚽', '⚾']
print(sport2)#['🥊', '🏈', '🏀', '⚽', '⚾', '🏐'] sport2 a desormer ça propre place en memoire


#ok maitenant voyons comment trouver un element dans une liste

print('🏀' in sport) #True

#Aggrandire une liste
sport3 = ['🏒']

sport2.extend(sport3)
print(sport2)#['🥊', '🏈', '🏀', '⚽', '⚾', '🏐', '🏒']

