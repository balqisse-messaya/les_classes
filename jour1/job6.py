class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom
        print(f"L'animal se nomme {self.prenom}")

animal = Animal()
print(f"L'âge de l'animal {animal.age} ans")  
animal.vieillir()
print(f"L'âge de l'animal {animal.age} ans") 
animal.nommer("Luna")  
