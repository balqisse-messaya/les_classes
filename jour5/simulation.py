
import random
from part import Part

def simulate_storm(ship):
    """Simule une tempête qui endommage aléatoirement une pièce du navire."""
    parts = list(ship._Ship__parts.values())
    if parts:
        damaged_part = random.choice(parts)
        damaged_part.change_material("Endommagé")
        print(f"La pièce {damaged_part.name} a été endommagée lors de la tempête!")

def simulate_wear_and_tear(ship):
    """Simule l'usure naturelle des pièces."""
    parts = list(ship._Ship__parts.values())
    if parts:
        worn_part = random.choice(parts)
        worn_part.change_material("Usé")
        print(f"La pièce {worn_part.name} est usée par l'usure.")
