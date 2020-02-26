# -*-coding:iso8859-15 -*

"""Ce module contient la classe Carte."""

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

	def getNom(self):
		return self.nom

	def getLab(self):
		print(self.lab)