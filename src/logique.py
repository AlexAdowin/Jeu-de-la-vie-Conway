
from .grille import Grille


class Logic :
    
    def __init__(self , grille: Grille):
        
        
        self.grille = grille
        
    def NombreVoisinsVivants ( self , ligne : int , colonne : int ) -> int :
        
        #compter le nombre de voisins vivants pour une cellule donnée 
        #considerer les cellules hors map comme morte  
        
        compteur = 0 
        
        lignes , colonnes = self.grille.obtenir_dimensions()
        
        #par rapport a la cellule obtenue iterer sur les 8 voisins
        
        for i in range(-1,2) :
            
            for j in range(-1,2) : 
                
                if i == 0 and j == 0 : 
                    
                    continue # ignore la cellule centrale 
                
                voisin_ligne , voisin_colonne = ligne  + i , colonne + j 
                
                #verifier si le voisin est dans les limites de la grille
                
                if 0 <= voisin_ligne < lignes and 0 <= voisin_colonne < colonnes :
                    
                    #si le voisin est vivant incrementer le compteur
                    if self.grille.obtenir_cellule (voisin_ligne , voisin_colonne) == 1 :
                        
                        compteur += 1 
                        
        return compteur
        
        
    def CalculerGenerationSuivante (self) -> Grille : 
        
        lignes , colonnes = self.grille.obtenir_dimensions() 
        
        nouvelle_grille = Grille (lignes , colonnes) 
        
        #parcours e chaque cellule de la grille actuelle
        
        for i in range (lignes) : 
            
            for j in range (colonnes) : 
                
                etat_actuel = self.grille.obtenir_cellule (i , j)
                
                nb_voisins = self.NombreVoisinsVivants (i , j)
                
                # la cellule conserve son etat patr defaut 
                
                nouvel_etat = etat_actuel
                
                # premiere regle : cellule meurt avec + 3 voisins et - 2 voisins
                
                if etat_actuel == 1 and (nb_voisins < 2 or nb_voisins > 3) : 
                    
                    nouvel_etat = 0
                    
                # deuxieme regle : cellule morte nait avec exactement 3 voisins vivants 
                
                elif etat_actuel == 0 and nb_voisins == 3 : 
                    
                    nouvel_etat = 1
                    
                # troisieme regle : cellule vivante survie avec 2 ou 3 voisins vivants
                # dans ce cas si les autres condition ne s'applique pas l'etat reste le meme
                
                nouvelle_grille.definir_cellule (i , j , nouvel_etat)
                
        return nouvelle_grille