class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    
    def perimetre(self):
        return 2 * (self._longueur + self._largeur)
    
    def surface(self):
        return self._longueur * self._largeur
    
    
    def getLongueur(self):
        return self._longueur
    
    def setLongueur(self, longueur):
        self._longueur = longueur
    
    def getLargeur(self):
        return self._largeur
    
    def setLargeur(self, largeur):
        self._largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
    
    def volume(self):
        return self.surface() * self._hauteur


rect = Rectangle(5, 3)
print("Périmètre:", rect.perimetre())
print("Surface:", rect.surface())

parallelepipede = Parallelepipede(5, 3, 4)
print("Volume:", parallelepipede.volume())
