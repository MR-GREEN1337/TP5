import numpy as np 

class Matrice():
    def __init__(self, nb_lignes: int, nb_colonnes: int, valeurs=None):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.valeurs = valeurs
    
    def nb_colonne(self):
        print(self.nb_colonnes)

    def nb_ligne(self):
        print(self.nb_lignes)

    def dimension(self):
        return [self.nb_lignes(), self.nb_colonnes()]

    def add(self, other):
        if self.nb_lignes != other.nb_lignes or self.nb_colonnes != other.nb_colonnes:
            raise ValueError("Les dimensions des matrices ne correspondent pas pour l'addition")

        result = Matrice(self.nb_lignes, self.nb_colonnes)
        for i in range(self.nb_lignes):
            for j in range(self.nb_colonnes):
                result.valeurs[i][j] = self.valeurs[i][j] + other.valeurs[i][j]
        return result

    def __add__(self, other):
        return self.add(other)    

    def trace(self):
        if self.nb_colonne != self.nb_lignes:
            return None
        
        else:
            result = 0

            for i in range(self.nb_lignes):
                for j in range(self.nb_colonnes):
                    if i==j:
                        result += self.valeurs[i][j]
            return result


if __name__ == "__main__":
    m1 = Matrice(2, 2, np.array([[1, 2], [3, 4]]))
    m2 = Matrice(2, 2, np.array([[5, 6], [7, 8]]))
    matrice = Matrice(1,2, m1)
    matrice2 = Matrice(1,2, m2)
    #matrice.nb_colonne()
    #matrice + matrice2
    m1 + m2


