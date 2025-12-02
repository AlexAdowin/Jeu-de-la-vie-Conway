import sys # Importation de sys pour une meilleure gestion de la sortie

class Grille:
    
    def __init__(self , lignes ,colonnes) :
        
        self.lignes = lignes
        
        self.colonnes = colonnes
        
        # Initialisation de la grille avec des cellules mortes (0)
        self.cellules = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)]
        
        
    def obtenir_cellule(self , ligne ,colonne) :
        
        if ligne < 0 or ligne >= self.lignes or colonne < 0 or colonne >= self.colonnes:
            
            raise IndexError("Index de cellule hors limites")
     
        return self.cellules[ligne][colonne]
        
        
    def definir_cellule(self , ligne ,colonne ,etat) :
         
         if ligne < 0 or ligne >= self.lignes or colonne < 0 or colonne >= self.colonnes:
             
             raise IndexError("Index de cellule hors limites")
         
         
         if etat not in (0 ,1) :
             
             raise ValueError("L'état de la cellule doit être 0 (morte) ou 1 (vivante)")
         
         self.cellules[ligne][colonne] = etat
         
    def obtenir_dimensions(self):
        
        return self.lignes , self.colonnes
    
    
    def reintialiser_grille(self):
        self.cellules = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)]

    def charger_depuis_fichier(self, etat_initial):
     
        try:
            with open(etat_initial, 'r') as fichier:
                lignes_fichier = fichier.readlines()
                
                for i, ligne in enumerate(lignes_fichier):
                    if i >= self.lignes:
                        break
                    
                    # On s'assure de gérer les lignes vides ou mal formatées
                    valeurs = ligne.strip().split() 
                    
                    for j, valeur in enumerate(valeurs):
                        if j >= self.colonnes:
                            break
                        
                        valeur_int = int(valeur)
                        if valeur_int not in (0, 1):
                            raise ValueError(f"Valeur invalide ({valeur}) à la ligne {i+1}, colonne {j+1}. Doit être 0 ou 1.")
                        
                        self.cellules[i][j] = valeur_int
            
            print(f"[OK] État initial chargé depuis '{etat_initial}' avec succès.")
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Le fichier d'état initial '{etat_initial}' est introuvable.")
        
        except ValueError as e:
            raise ValueError(f"Erreur de format dans le fichier : {e}")
        
        # Supprimons le bloc Exception générique pour une meilleure clarté.
        # Les erreurs inattendues seront gérées plus haut dans la pile d'appels.
