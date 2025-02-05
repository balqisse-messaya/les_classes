class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Point: ({self.x}, {self.y})")

    def afficherX(self):
        print(f"X: {self.x}")

    def afficherY(self):
        print(f"Y: {self.y}")

    def changerX(self, nouvelleX):
        self.x = nouvelleX

    def changerY(self, nouvelleY):
        self.y = nouvelleY

point = Point(3, 4)
point.afficherLesPoints()  
point.afficherX()  
point.afficherY()  
point.changerX(10)
point.changerY(12)
point.afficherLesPoints()  
