class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

produit1 = Produit("Produit1", 100, 20)
produit1.afficher()  
print(f"Prix TTC: {produit1.CalculerPrixTTC()}")

produit1.modifierNom("Produit2")
produit1.modifierPrix(120)
produit1.afficher()  
