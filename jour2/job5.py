class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  

    
    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:  
            self.__en_marche = True
            print(f"La voiture {self.__marque} {self.__modele} a démarré.")
        else:
            print("Erreur: Réservoir insuffisant pour démarrer.")

    def arreter(self):
        self.__en_marche = False
        print(f"La voiture {self.__marque} {self.__modele} est arrêtée.")

    def __verifier_plein(self):
        return self.__reservoir  

    
    def remplir_reservoir(self, quantite):
        if quantite > 0:
            self.__reservoir += quantite
            print(f"Le réservoir a été rempli avec {quantite} litres.")
        else:
            print("Erreur: Quantité de carburant invalide.")


voiture = Voiture("Toyota", "Corolla", 2020, 15000)
voiture.demarrer()  
voiture.remplir_reservoir(10)  
voiture.demarrer()  
voiture.arreter()  

