class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre= titre
        self.__auteur= auteur
        self.__nb_pages= nb_pages

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur= auteur

    def set_nb_pages(self, nb_pages):
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else: 
            print("Erreur: Lenombre de pages doit etre un entier positif. ")

livre = Livre("Titre A", "Auteur A", 300)
livre.set_nb_pages(350)
print("Titre:", livre.get_titre())
print("Auteur:", livre.get_auteur())
print("Nombre de pages:", livre.get_nb_pages())

livre.set_nb_pages(-100)