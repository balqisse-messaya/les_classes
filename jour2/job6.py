class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}
        self.__statut = "en cours"

    
    def ajouter_plat(self, nom_plat, prix):
        self.__plats[nom_plat] = {"prix": prix, "statut": "en cours"}

    def annuler_commande(self):
        self.__statut = "annulée"
        print("Commande annulée")

    def __calculer_total(self):
        return sum(plat['prix'] for plat in self.__plats.values())

    def afficher_commande(self):
        print(f"Commande {self.__numero_commande} - Statut: {self.__statut}")
        for plat, details in self.__plats.items():
            print(f"{plat}: {details['prix']}€")
        print("Total:", self.__calculer_total(), "€")

    def calculer_tva(self):
        return self.__calculer_total() * 0.2 


commande = Commande(123)
commande.ajouter_plat("Pizza", 10)
commande.ajouter_plat("Pâtes", 15)
commande.afficher_commande()
