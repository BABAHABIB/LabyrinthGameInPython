# -*-coding:iso8859-15 -*

"""Ce module contient la classe Carte."""

import os

from Fonctions.Librairies import *
from labyrinthe import *

class Carte:

	#Indicateur du nombre de cartes disponibles
	nbr_cartes = 0

	def __init__(self,nom,started):
		self.nom = nom
		#Indicateur cartes commencée ou pas
		self.started = started
		Carte.nbr_cartes += 1
		self.lab = Labyrinthe(nom,started)

	def getLab(self):
		print(self.lab)

	def __del__(self):
		#print("Partie existante sur la carte ",self.nom," est supprimée")
		if Carte.nbr_cartes > 0:
			Carte.nbr_cartes -= 1
		else:
			Carte.nbr_cartes = 0
		#Suppression de la partie
		del_partie(self.nom)

#a = Carte("prison",False)
#b = Carte("prison")
#print(Carte.nbr_cartes)
#a.getLab()
#print(34335)
#os.system("PAUSE")