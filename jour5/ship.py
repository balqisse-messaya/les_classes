
from part import Part

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}

    def add_part(self, part):
        """Ajoute une pièce au navire."""
        self.__parts[part.name] = part

    def display_state(self):
        """Affiche l'état du navire (toutes les pièces et leur matériau)."""
        print(f"État du navire '{self.name}':")
        for part in self.__parts.values():
            print(part)

    def replace_part(self, part_name, new_part):
        """Remplace une pièce existante par une nouvelle."""
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
        else:
            print(f"La pièce {part_name} n'existe pas.")


class ShipWithHistory(Ship):
    def __init__(self, name):
        super().__init__(name)
        self.history = []

    def replace_part(self, part_name, new_part):
        """Remplace une pièce et enregistre cette modification dans l'historique."""
        super().replace_part(part_name, new_part)
        self.history.append(f"Remplacement de {part_name} par {new_part.name} ({new_part.material})")

    def show_history(self):
        """Affiche l'historique des modifications."""
        print(f"Historique des modifications du navire '{self.name}':")
        for event in self.history:
            print(event)
