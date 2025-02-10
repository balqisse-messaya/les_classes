# part.py

class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        """Change le matériau de la pièce."""
        self.material = new_material

    def __str__(self):
        """Retourne une description de la pièce."""
        return f"Partie: {self.name}, Matériau: {self.material}"

