
import tkinter as tk
from part import Part
from ship import ShipWithHistory

class ShipApp:
    def __init__(self, root, ship):
        self.ship = ship
        self.root = root
        self.root.title(f"Gestion du navire: {ship.name}")

        self.display_state_button = tk.Button(root, text="Afficher l'état du navire", command=self.display_state)
        self.display_state_button.pack()

        self.replace_part_button = tk.Button(root, text="Remplacer une pièce", command=self.replace_part)
        self.replace_part_button.pack()

    def display_state(self):
        """Affiche l'état du navire dans la fenêtre."""
        state_text = "\n".join(str(part) for part in self.ship._Ship__parts.values())
        state_label = tk.Label(self.root, text=f"État du navire:\n{state_text}")
        state_label.pack()

    def replace_part(self):
        """Permet à l'utilisateur de remplacer une pièce (interface basique)."""
        part_name = input("Entrez le nom de la pièce à remplacer: ")
        new_material = input("Entrez le nouveau matériau: ")
        new_part = Part(part_name, new_material)
        self.ship.replace_part(part_name, new_part)

def start_ui():
    navire = ShipWithHistory("Navire de Thésée")
    mât = Part("Mât", "Bois")
    coque = Part("Coque", "Bois")
    navire.add_part(mât)
    navire.add_part(coque)

    root = tk.Tk()
    app = ShipApp(root, navire)
    root.mainloop()

if __name__ == "__main__":
    start_ui()
