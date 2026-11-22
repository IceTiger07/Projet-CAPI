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

    def setVote(self, newVote):
        if newVote not in liste_cartes:
            raise Exception("Vote invalide !")
        else :
            self.vote = newVote


def configuration(liste_joueurs):
    nombre_joueurs = int(input("Saisir le nombre de joueur : "))
    for i in range(nombre_joueurs):
        saisirPseudo = input("Saisissez votre pseudo : ")
        liste_joueurs.append(Joueur(saisirPseudo," "))

def charger_fichier_json():
    with open('exemples/exemple_bibliothèque.json', 'r', encoding='utf-8') as exemple:
        contenu = json.load(exemple)
    for ligne in contenu["fonctionnalites"]:
        if ligne["id"] == "F1":
            print(ligne["titre"])

def vote_cache(liste_joueurs):
    for joueur in liste_joueurs:
        messageSaisi = "Joueur " + joueur.getPseudo() + ", saississez votre vote : "
        saisirVote = str(input(messageSaisi))
        joueur.setVote(saisirVote)

def reinit_vote(liste_joueurs):
    for joueur in liste_joueurs:
        joueur.setVote(" ")

def recup_vote(liste_joueurs,liste_vote):
    for resultat in liste_joueurs:
        liste_vote.append(resultat.getVote())
    return liste_vote

def revelation_vote(liste_vote):
    for resultat in liste_vote:
        print(resultat)
    
# retourne un entier : -1 si on revote, x si on a une valeur retenue où x est la valeur retenue
def validation_vote(liste_vote,regle,tour):
    match regle:
        case "strict":
            compareVote = liste_vote[0]
            for i in range (1, len(liste_vote)):
                if compareVote != liste_vote[i]:
                    return -1
            return int(compareVote[0])
        case "moyenne":
            if tour == 1:
                compareVote = liste_vote[0]
                for i in range (1, len(liste_vote)):
                    if compareVote != liste_vote[i]:
                        return -1
                return int(compareVote[0])
            elif tour == 2:
                resultat = calcul_moyenne(liste_vote)
                return resultat
                
def calcul_moyenne(liste_vote):
    nb_vote = len(liste_vote)
    resultat = 0
    for i in range (nb_vote):
        resultat += int(liste_vote[i])
    resultat = resultat/nb_vote
    if str(resultat) in liste_cartes:
        return resultat
    else :
        liste_vote.sort()
        if nb_vote%2 == 1:
            return liste_vote[nb_vote%2 -0.5]
    
if __name__ == "__main__":
    liste_joueurs = []
    configuration(liste_joueurs)
    charger_fichier_json()
    print(liste_joueurs[0].getPseudo())
