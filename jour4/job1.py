class Personne:
    def __init__(self, age=14):
        self._age = age

    def afficherAge(self):
        print(f"L'âge de la personne est {self._age} ans.")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, age):
        self._age = age

class Eleve(Personne):
    def __init__(self, age=14):
        super().__init__(age)
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J’ai {self._age} ans")

class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self._matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")


eleve = Eleve()
eleve.afficherAge()

eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.afficherAge()

professeur = Professeur(age=40, matiereEnseignee="Mathématiques")
professeur.bonjour()
professeur.enseigner()
