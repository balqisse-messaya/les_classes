import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(10, 30)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} dégâts!")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = 0

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 = facile, 2 = moyen, 3 = difficile): "))

    def lancer_jeu(self):
        if self.niveau == 1:
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 80)
        elif self.niveau == 2:
            joueur = Personnage("Joueur", 80)
            ennemi = Personnage("Ennemi", 80)
        else:
            joueur = Personnage("Joueur", 60)
            ennemi = Personnage("Ennemi", 100)

        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)

        if joueur.est_vivant():
            print("Le joueur a gagné!")
        else:
            print("L'ennemi a gagné!")


jeu = Jeu()
jeu.choisir_niveau()
jeu.lancer_jeu()
