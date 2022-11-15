# python3
import os
import random
os.system('clear')

# Bienvenue & explication des règles
print("Bienvenue sur le jeu des Bâtonnets")
regles = eval(input("Entrez 1 pour lire les règles si non entrez 0 : "))
if regles==1:
	print(" 1 - Vous avez la possibilité de jouer contre un ordinateur ou un ami \n 2 - Le but du jeu est de forcer l'adversaire à prendre le dernier bâtonnet présent \n 3 - Vous jouez chacun votre tour \n 4 - A chaque tour vous pouvez prendre en 1 et 3 bâtonnets \n 5 - Amusez-vous bien et beaucoup 😉")
	
	
# Toute la partie jeu / joueurs / bot
class JeuDesBattons:
	def __init__(self , batonnet, joueurs , tour=-1):
		self.tour = tour
		self.batonnet = batonnet
		self.joueurs = joueurs
	def aQuiDeJouer(self):
		self.tour += 1
		if self.joueurs == 0:
			if self.tour%2==0:
				print("Au Joueur1 de jouer !")
				nouveauJeu.JouerJoueur("Joueur1")
			else:
				print("A Joueur2 de jouer !")
				nouveauJeu.JouerJoueur("Joueur2")
		else:
			if self.tour%2==0:
				print("A toi de jouer !")
				nouveauJeu.JouerJoueur("Joueur")
			else:
				print("Le bot à jouer !")
				nouveauJeu.JouerBot()
				
	def JouerJoueur(self, qui):
		prendre = 0
		while prendre<1 or prendre>3 :
			prendre = int(input("Entrez le nombre de bâtonnet que vous souhaitez prendre : "))
		self.batonnet -= prendre
		nouveauJeu.jeu(qui)
		
	def JouerBot(self):
		self.batonnet -= random.randint(1, 3)
		nouveauJeu.jeu("Bot")
		
	def jeu(self, qui):
		if self.batonnet<=0:
			print("Le ", qui ," a perdu !")
		else:
			os.system('clear')
			print("Il reste ", self.batonnet," bâtonnets :")
			print(" | "*self.batonnet)
			nouveauJeu.aQuiDeJouer()

#Initialisation du Jeu
batonnets = 0
while batonnets%2!=1:
	batonnets = eval(input("Le nombre de bâtonnets que vous souhaitez sur le plateau de jeu : "))
joueurs = eval(input("Entrez 1 pour jouer contre l'ordinateur et 0 pour jouer contre un ami : "))
print("Il reste ",batonnets," bâtonnets :")
print(" | "*batonnets)
nouveauJeu = JeuDesBattons(batonnets, joueurs)
nouveauJeu.aQuiDeJouer()