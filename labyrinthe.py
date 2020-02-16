# -*-coding:iso8859-15 -*

from Fonctions.Librairies import *

"""Ce module contient la classe Labyrinthe."""
class Labyrinthe:

	def __init__(self,nom,started):
		self.nom = nom
		self.robot = "X"
		self.grille = creer_labyrinthe_depuis_chaine(nom,started)
		self.porte = "."
		self.mur = "O"
		self.sortie = "U"
		self.position = get_robot_position(self.grille,self.robot)
		self.previousObstacle = getPreviousObstacle(nom)

	def getPosition(self):
		return self.position

	def update_lab(self,new_position):
		i,j = self.position[0],self.position[1]
		e,f = new_position[0],new_position[1]
		self.grille[i,j] = self.previousObstacle
		self.previousObstacle = self.grille[e,f]
		setPreviousObstacle(self.nom,self.previousObstacle)
		self.grille[e,f] = self.robot
		self.position = new_position

	def Check_Obstacle(self,new_position):
		if self.grille[new_position] in [self.mur,chariot] :
			return 0 #"Impossible"
		if self.grille[new_position] in [self.porte," "]:
			self.update_lab(new_position)
			update_labyrinthe_depuis_grille(self.nom,self.grille)
			return 1 #"Deplacement OK"
		if self.grille[new_position] == self.sortie:
			self.update_lab(new_position)
			update_labyrinthe_depuis_grille(self.nom,self.grille)
			return 2 # You win carte deleted

	def __repr__(self):
		return afficher_partie(self.nom)