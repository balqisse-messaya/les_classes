class Student:
    def __init__(self, nom, prenom, id_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__id_etudiant = id_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    
    def get_credits(self):
        return self.__credits

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom: {self.__nom}     Prenom: {self.__prenom}     id:{self.__id_etudiant}     Niveau: {self.__level}")


etudiant = Student("Jonh", "Doe", 145)
etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.student_info()  
