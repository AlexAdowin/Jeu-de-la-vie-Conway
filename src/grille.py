
class Grille:
    
    def __init__(self , lignes ,colonnes) :
        
        self.lignes = lignes
        
        self.colonnes = colonnes
        
        self.cellules = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)] # Initialisation de la grille avec des cellules mortes (0)
        
        
    def obtenir_cellule(self , ligne ,colonne) :
        
        if ligne < 0 or ligne >= self.lignes or colonne < 0 or colonne >= self.colonnes:
            
            raise 0
     
        
        
        return self.cellules[ligne][colonne]
        
        
    def definir_cellule(self , lignes ,colonnes ,etat) :
         
         if lignes < 0 or lignes >= self.lignes or colonnes < 0 or colonnes >= self.colonnes:
             
             raise IndexError("Index de cellule hors limites")
         
         
         if etat not in (0 ,1) :
             
             raise ValueError("L'état de la cellule doit être 0 (morte) ou 1 (vivante)")
         
         self.cellules[lignes][colonnes] = etat
         
    def obtenir_dimensions(self):
        
        
        
        return self.lignes , self.colonnes
    
    
    def reintialiser_grille(self):
        
        self.cellules = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)] # Réinitialisation de la grille avec des cellules mortes (0)
