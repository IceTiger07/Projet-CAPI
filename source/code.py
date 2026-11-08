import json

class Joueur:
    def __init__(self, pseudo):
        self.pseudo = pseudo

    def getPseudo(self):
        return self.pseudo

def configuration(liste_joueurs):
    nombre_joueurs = input("Saisir le nombre de joueur : ")
    for i in range(nombre_joueurs):
        saisirPseudo = input("Saisissez votre pseudo : ")
        liste_joueurs.append(Joueur(saisirPseudo))

def charger_fichier_json():
    with open('exemples/exemple_bibliothèque.json', 'r', encoding='utf-8') as exemple:
        contenu = json.load(exemple)
    print(contenu)

liste_joueurs = []
configuration(liste_joueurs)
charger_fichier_json()
 