
from grille import Grille


class Logic :
    
    def __init__(self):
        
        self.grille = Grille(50 ,50)    
        
    def getCellulePosition(self ) : 
        
        live = []
        
        for x in range (self.ligne) :
            
            for y in range (self.colonne) :
                
                if self.grille[x][y] == 1 :
                    
                    live.append(( x , y ))
        return live    
    
    
    def NombreVoisinsVivants(self , live , x , y) :
      
        compteur = 0
        
        # Les 8 positions voisines
        voisins = [
            (x-1, y+1),  # haut-gauche
            (x,   y+1),  # haut
            (x+1, y+1),  # haut-droite
            (x-1, y),    # gauche
            (x+1, y),    # droite
            (x-1, y-1),  # bas-gauche
            (x,   y-1),  # bas
            (x+1, y-1)   # bas-droite
        ]
        
        for voisin in voisins:
            if voisin in live:  # Vérifier si le voisin est dans la liste des cellules vivantes
                compteur += 1
        
        return compteur
        
        
    def CycleCellule(self , compteur , live ) :        
        
        if compteur == 2 :
            
            return 1
        
        elif compteur == 3 : 
            
            
            
            
    
    
    

    def CalculerGenerationSuivante (self) :
        
        pass
    
    