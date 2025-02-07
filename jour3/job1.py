class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def ajouter_population(self):
        self.__nb_habitants += 1

    def get_nb_habitants(self):
        return self.__nb_habitants


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(f"Population de la ville de Paris : {paris.get_nb_habitants()} habitants")
print(f"Population de la ville de Marseille : {marseille.get_nb_habitants()} habitants")


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouter_population(self):
        self.ville.ajouter_population()


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()


print(f"Mise à jour de la population de la ville de Paris {paris.get_nb_habitants()} habitants")
print(f"Mise à jour de la population de la ville de Marseille {marseille.get_nb_habitants()} habitants")
