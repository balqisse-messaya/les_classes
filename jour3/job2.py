class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.__numero_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Solde: {self.__solde}")

    def afficher_solde(self):
        print(f"Solde actuel: {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€. Nouveau solde: {self.__solde}€")

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur: Montant insuffisant.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€. Nouveau solde: {self.__solde}€")

    def agios(self):
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.1
            self.__solde -= frais
            print(f"Agios appliqués: {frais}€. Nouveau solde: {self.__solde}€")

    def virement(self, compte_dest, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant}€ vers le compte {compte_dest.__numero_compte}")
        else:
            print("Erreur: Montant insuffisant pour le virement.")


compte1 = CompteBancaire(12345, "Dupont", "Pierre", 500)
compte2 = CompteBancaire(67890, "Martin", "Marie", -100, True)


compte1.afficher()
compte1.versement(200)
compte1.retrait(100)
compte1.afficher_solde()
compte1.agios()

compte1.virement(compte2, 300)
compte2.afficher_solde()
