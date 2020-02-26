import os
import re
from shutil import copy2
########################## Settings ##########################

###paths
#os.chdir('../')
partiesbkp = os.getcwd() + "\cartesbkp"
partiessaved = os.getcwd() + "\partiessaved"
chemin_obstacle= os.getcwd() + "\Obstacles\\"
#Variables
extension = ".txt"
chemin = partiessaved
fic_name = chemin + "\\"
chariot = "\n"
####expressions regulières
reg = "[CcNnqQ]{1}"
#Deplacements Possibles
D_P = "[SsNnEeOoQq]{1}"
obstacles = [' ','O']

########################## Settings ##########################

def getparties(started):
	if started == True:
		print("Labyrinthes entamés - parties commencés :")
		chemin = partiessaved
	else:
		print("Labyrinthes disponibles :")
		chemin = partiesbkp
	i = 0
	for nom_fichier in os.listdir(chemin):
		#print(nom_fichier)
		print("  {} - {}".format(i+1, nom_fichier))
		i +=1

def PartieExiste(nom,started):
	if started == True:
		chemin = partiessaved
	else:
		chemin = partiesbkp

	if os.path.isfile(chemin+"\\"+nom+extension):
		return True
	else:
		return False

def creer_labyrinthe_depuis_chaine(nom,started):
	if started == False:
		create_partie(nom)
	i= 0
	grille = {}
	with open(fic_name+nom+extension, 'r') as f:
		for line in f:
			j = 0
			for ch in line:
				grille[i,j]= ch
				j += 1
			i += 1
	f.close()
	return grille

def get_Next_position(position,action):
	i,j = position[0],position[1]
	#Sud
	if action.upper() == D_P[1]:
		i += 1
	#Nord
	if action.upper() == D_P[3]:
		i -= 1
	#Est
	if action.upper() == D_P[5]:
		j += 1
	#Ouest
	if action.upper() == D_P[7]:
		j -= 1

	new_position = i,j
	return new_position

def update_labyrinthe_depuis_grille(nom,grille):
	ch =""
	for position, value in grille.items():
		ch += value
	f= open(fic_name+nom+extension, 'w')
	f.write(ch)
	f.close()

def create_partie(nom):
	if os.path.exists(chemin_obstacle+nom+extension):
		os.remove(chemin_obstacle+nom+extension)
	copy2(partiesbkp+"\\"+nom+extension,chemin)

def afficher_partie(nom):
	with open(fic_name+nom+extension, "r") as f:
		cont = f.read()
	f.close()
	return(cont)

def get_robot_position(grille,robot):
		for position, value in grille.items():
			if value == robot:
				return position

def setPreviousObstacle(nom,previous_obstacle):
	f= open(chemin_obstacle+nom+extension, 'w+')
	f.write(previous_obstacle)
	f.close()

def getPreviousObstacle(nom):
	if not os.path.exists(chemin_obstacle+nom+extension):
		with open(chemin_obstacle+nom+extension, 'w') as f: pass

	f = open(chemin_obstacle+nom+extension, 'r')
	previous_obstacle = f.read()
	f.close()
	if previous_obstacle == "":
		previous_obstacle = " "
	return previous_obstacle