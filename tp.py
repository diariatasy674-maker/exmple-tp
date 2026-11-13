from abc import ABC, abstractmethod

from p_poo_NOM_Prenom import enseignant


class personne (ABC):
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom

def nom_complet(self):
    return f"{self.prenom} {self.nom}"

abstractmethod
def role (self);
    self

    class etudiante (personne):
    def __init__(self,nom ,prenom ,matricule):
        super().__init__(nom,prenom)
        self.matricule=matricule
        self._notes=[]

        @property
        def matricule(self):
            return self.matricule

        def moyene (self):
            if len(self._notes) == 0:
                return 0
            return sum(self._notes) / len(self._notes)

        def role etudiante(self):
            return "Etudiante"
    
    class enseignant (personne):
        def __init__(self,nom ,prenom ,salaire ,taux_hauraire):
            super().__init__(nom,prenom)
            self.salaire= salaire
            self.taux_hauraire=taux_hauraire

        def calculer_salaire (self):
            return self.salaire * self.taux_hauraire

        def role_enseignant(self):
            return "Enseignant"



if __name__ == "__main__":
    etu = etudiante("sy", "Diarieta", "M001")
    etu._notes.append(14)
    etu._notes.append(17)
    print(f"Nom complet: {etu.nom_complet()}")
    print(f"Matricule: {etu.matricule}")
    print(f"Moyenne: {etu.moyene()}")
    print(f"Role: {etu.role()}")

    prof = enseignant("sow", "salif", 2000, 45)
    print(f"Nom complet: {prof.nom_complet()}")
    print(f"Salaire: {prof.calculer_salaire()}")
    print(f"Role: {prof.role_enseignant()}")
