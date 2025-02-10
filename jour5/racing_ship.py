
from ship import Ship

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)  
        self.max_speed = max_speed

    def display_speed(self):
        """Affiche la vitesse maximale du navire de course."""
        print(f"Vitesse maximale du navire '{self.name}': {self.max_speed} km/h")
