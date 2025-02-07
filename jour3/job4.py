class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts += 1

    def effectuer_une_passe_decisive(self):
        self.passes += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        print(f"{self.nom} (Numéro {self.numero}, {self.position})")
        print(f"Buts: {self.buts}, Passes décisives: {self.passes}, Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        for joueur in self.joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        joueur.buts += buts
        joueur.passes += passes
        joueur.cartons_jaunes += cartons_jaunes
        joueur.cartons_rouges += cartons_rouges


joueur1 = Joueur("Léo", 10, "Attaquant")
joueur2 = Joueur("Marc", 5, "Défenseur")
equipe1 = Equipe("FC Paris")


equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)


joueur1.marquer_un_but()
joueur2.recevoir_un_carton_jaune()
equipe1.afficher_statistiques_joueurs()
