# -*-coding:iso8859-15 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
#Librairies
import os
import re
from carte import Carte
from Fonctions.Librairies import *
###Variables
continuer_partie = True
ok = False
###Variables

############# Banderole d'acceuil du Jeu #############
print("*********************************************")
print("Bonjour et bienvenue sur le jeu du labyrinthe")
print("*********************************************")
print("\n")
############# Banderole d'acceuil du Jeu #############

getparties(True)
print("\n")
getparties(False)
print("\n")
while continuer_partie:

	print("Souhaitez vous jouer une nouvelle partie ou continuer sur une partie existante ?")
	user_entry = input("N = Nouvelle, C = Continuer une partie, Q = Quitter le jeu \n")

	if re.match(reg,user_entry):
		if user_entry.upper() == "Q":
			continuer_partie = False
			break
		if user_entry.upper() == "N":
			started = False
		if user_entry.upper() == "C":
			started = True
	else:
		print("Le choix saisi est incorrect, veuillez recommencer")
		continue

	while ok == False :
		nom= input("Veuillez entrer le nom de la partie à jouer: ")
		ok = PartieExiste(nom,started)
	
	partie = Carte(nom,started)
	partie.getLab()
	ok = False
	while ok == False :
		action = input("Entrez un deplacement N=Nord, S=Sud, E=Est, O=Ouest:")
		if re.match(D_P,action):
			print("deplacement OK")
			deplacement(partie.lab)
		else:
			print("Le choix saisi est incorrect, veuillez recommencer")
			continue


print("Au revoir et à bientot")
os.system("PAUSE")