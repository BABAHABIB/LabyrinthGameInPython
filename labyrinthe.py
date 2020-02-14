# -*-coding:iso8859-15 -*

import os

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
		self.previousObstacle = " "


	def getNom(self):
		print(self.nom)

	def getRobot(self):
		print(self.position)

	def setPreviousObstacle(Obstacle):
		self.previousObstacle = Obstacle

	def get_Next_position(self,action):
		i,j = self.position[0],self.position[1]
		#Sud
		if action.upper() == D_P[0]:
			i += 1
		#Nord
		if action.upper() == D_P[2]:
			i -= 1
		#Est
		if action.upper() == D_P[4]:
			j += 1
		#Ouest
		if action.upper() == D_P[6]:
			j -= 1

		new_position = i,j

		return new_position

	def Check_Obstacle(self,new_position):
		if self.grille[new_position] in [self.mur,chariot] :
			print("Deplacement impossible il s'agit d'un obstacle")
			return 0 #"Impossible"
		if self.grille[new_position] == self.porte:
			return 1 #"Deplacement OK"
		if self.grille[new_position] == self.sortie:
			return 2 # You win carte deleted

	def update_grille(self,new_position):
		i,j = self.position[0],self.position[1]
		e,f = new_position[0],new_position[1]
		self.grille[i,j] = self.previousObstacle
		print(self.grille[i,j])
		self.previousObstacle = self.grille[e,f]
		self.grille[e,f] = self.robot

	def __repr__(self):
		return afficher_partie(self.nom)

nom = "facile"
lab = Labyrinthe(nom,False)
print(lab.grille)
print(lab.position)
new_position = (4,8)
print(lab.position[0],lab.position[1])
lab.update_grille(new_position)
print(lab.grille)
print(lab.previousObstacle)
update_labyrinthe_depuis_grille(lab.nom,lab.grille)
#print(lab)
#print(lab.position)
#print(lab.previousObstacle)
#update_labyrinthe_depuis_grille(lab.nom,lab.grille)
os.system("PAUSE")
