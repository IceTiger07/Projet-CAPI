import json

liste_cartes = ["0", "1/2", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "café"]

class Joueur:

    def __init__(self, pseudo, vote):
        self.pseudo = pseudo
        self.vote = vote

    def getPseudo(self):
        return self.pseudo

    def getVote(self):
        return self.vote


def configuration(liste_joueurs):
    nombre_joueurs = int(input("Saisir le nombre de joueur : "))
    for i in range(nombre_joueurs):
        saisirPseudo = input("Saisissez votre pseudo : ")
        liste_joueurs.append(Joueur(saisirPseudo))

def charger_fichier_json():
    with open('exemples/exemple_bibliothèque.json', 'r', encoding='utf-8') as exemple:
        contenu = json.load(exemple)
    for ligne in contenu["fonctionnalites"]:
        if ligne["id"] == "F1":
            print(ligne["titre"])

def vote_cache(liste_joueurs):
    
    
# retourne un entier : -1 si on revote, x si on a une valeur retenue où x est la valeur retenue
def validation_vote(liste_vote,regle,tour):
    raise Exception("non implémenté") 
    
if __name__ == "__main__":
    liste_joueurs = []
    configuration(liste_joueurs)
    charger_fichier_json()
    print(liste_joueurs[0].getPseudo())
