
class Grille:
    
    def __init__(self , lignes ,colonnes) :
        
        self.lignes = 50
        
        self.colonnes = 50 
        
        self.cellules = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)] # Initialisation de la grille avec des cellules mortes (0)
        
        
    def obtenir_cellule(self , lignes ,colonnes) :
        
        
        
        return self.cellules[lignes][colonnes]
        
        
    def definir_cellule(self , lignes ,colonnes ,etat) :
         
         
         self.cellules[lignes][colonnes] = etat
         
    def obtenir_dimensions(self):
        
        
        return self.lignes , self.colonnes
