class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, tache):
        self.taches.remove(tache)

    def marquer_comme_finie(self, tache):
        tache.statut = "terminée"

    def afficher_liste(self):
        for tache in self.taches:
            print(tache)

    def filter_liste(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


tache1 = Tache("Faire les courses", "Acheter des légumes")
tache2 = Tache("Étudier", "Réviser pour l'examen", "terminée")
liste = ListeDeTaches()
liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)


liste.afficher_liste()


taches_a_faire = liste.filter_liste("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)


liste.marquer_comme_finie(tache1)
print("\nListe après mise à jour des tâches :")
liste.afficher_liste()
