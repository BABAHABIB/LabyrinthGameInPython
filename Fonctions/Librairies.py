import os
import re
from shutil import copy2
########################## Settings ##########################

###paths
#os.chdir('../')
partiesbkp = os.getcwd() + "\cartesbkp"
partiessaved = os.getcwd() + "\partiessaved"

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
		print("Labyrinthes entamés - parties commencées :")
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
		print("Partie introuvable, veuillez recommencer !")
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

def update_labyrinthe_depuis_grille(nom,grille):
	ch =""
	for position, value in grille.items():
		ch += value
	f= open(fic_name+nom+extension, 'w')
	f.write(ch)
	f.close()

def del_partie(nom):
	os.remove(fic_name+nom+extension)
	copy2(partiesbkp+"\\"+nom+extension,chemin)

def create_partie(nom):
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

#def deplacerRobot(grille,action)
#
#	if next_pos in {'','','',''}
#def multipli (x,y):
#	return x * y

#cont = afficher_partie("prison")
#print(cont)
#os.system("PAUSE")