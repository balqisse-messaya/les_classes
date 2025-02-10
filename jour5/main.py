
from part import Part
from ship import Ship, ShipWithHistory
from racing_ship import RacingShip

def main():
    
    mât = Part("Mât", "Bois")
    coque = Part("Coque", "Bois")

    navire = ShipWithHistory("Navire de Thésée")
    navire.add_part(mât)
    navire.add_part(coque)

    
    navire.display_state()

    
    navire.replace_part("Mât", Part("Mât", "Acier"))
    navire.replace_part("Coque", Part("Coque", "Aluminium"))


    print("\nÉtat après modifications:")
    navire.display_state()

    
    print("\nHistorique des changements:")
    navire.show_history()

    
    racing_ship = RacingShip("Navire de Course", 150)
    racing_ship.add_part(mât) 
    racing_ship.display_state()  
    racing_ship.display_speed() 

if __name__ == "__main__":
    main()
