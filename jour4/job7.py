import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def valeurCarte(self):
        if self.valeur in ['J', 'Q', 'K']:
            return 10
        elif self.valeur == 'A':
            return 1  
        return int(self.valeur)

class Jeu:
    def __init__(self):
        
        self.paquet = [Carte(str(i), couleur) for i in range(2, 11) for couleur in ['Coeur', 'Carreau', 'Trèfle', 'Pique']]
        self.paquet += [Carte(valeur, couleur) for valeur in ['J', 'Q', 'K', 'A'] for couleur in ['Coeur', 'Carreau', 'Trèfle', 'Pique']]
        random.shuffle(self.paquet)

    def distribuerCarte(self):
        return self.paquet.pop()

    def calculeValeurMain(self, main):
        total = sum([carte.valeurCarte() for carte in main])
        
        for carte in main:
            if carte.valeur == 'A' and total + 10 <= 21:
                total += 10
        return total

    def jouer(self):
        joueur_main = [self.distribuerCarte(), self.distribuerCarte()]
        croupier_main = [self.distribuerCarte(), self.distribuerCarte()]

        
        print("Main du joueur:", [carte.valeur for carte in joueur_main])
        print("Main du croupier:", [carte.valeur for carte in croupier_main])

        
        while self.calculeValeurMain(joueur_main) < 21:
            choix = input("Voulez-vous 'prendre' une carte ou 'passer' ? ").lower()
            if choix == 'prendre':
                joueur_main.append(self.distribuerCarte())
                print("Main du joueur:", [carte.valeur for carte in joueur_main])
            else:
                break

        
        while self.calculeValeurMain(croupier_main) < 17:
            croupier_main.append(self.distribuerCarte())

        print("Main du croupier:", [carte.valeur for carte in croupier_main])

        
        joueur_total = self.calculeValeurMain(joueur_main)
        croupier_total = self.calculeValeurMain(croupier_main)

        print(f"Total du joueur: {joueur_total}")
        print(f"Total du croupier: {croupier_total}")

        if joueur_total > 21:
            print("Le joueur a perdu, dépassement de 21.")
        elif croupier_total > 21:
            print("Le croupier a perdu, dépassement de 21.")
        elif joueur_total > croupier_total:
            print("Le joueur gagne!")
        elif joueur_total < croupier_total:
            print("Le croupier gagne!")
        else:
            print("C'est une égalité!")


jeu = Jeu()
jeu.jouer()

