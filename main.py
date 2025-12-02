#  Créer une grille initiale.
#  Charger un état initial depuis etat_initial.txt si vous en avez un, sinon il initialise un "blinker" simple pour tester.
#  Initialiser la logique du jeu.
#  Initialiser l'affichage Pygame.
#  Exécuter une boucle principale qui calcule les générations successives et les affiche.

import pygame
import sys
import time
from src.grille import Grille
from src.logique import Logic
from src.affichage import AfficheGrille

#parametre de simulation 

TAILLE_GRILLE = 50

FICHIER_ETAT_INITIAL = "src/etat_initial.txt"  

VITESSE_FPS = 3.5

def main()  :
    
    #initiliser la grille 
    
    grille = Grille (TAILLE_GRILLE, TAILLE_GRILLE)
    
    # 2. Chargement de l'état initial ou configuration d'un exemple
    try:
        grille.charger_depuis_fichier(FICHIER_ETAT_INITIAL)
    except FileNotFoundError:
        print(f"[ATTENTION] Fichier d'état initial '{FICHIER_ETAT_INITIAL}' non trouvé. Utilisation d'un Blinker comme exemple.")
        # Exemple simple: un Blinker (période 2)
        grille.definir_cellule(TAILLE_GRILLE // 2 - 1, TAILLE_GRILLE // 2, 1)
        grille.definir_cellule(TAILLE_GRILLE // 2, TAILLE_GRILLE // 2, 1)
        grille.definir_cellule(TAILLE_GRILLE // 2 + 1, TAILLE_GRILLE // 2, 1)
    except Exception as e:
        print(f"[ERREUR] Erreur lors du chargement de l'état initial : {e}. Utilisation d'un Blinker.")
        grille.definir_cellule(TAILLE_GRILLE // 2 - 1, TAILLE_GRILLE // 2, 1)
        grille.definir_cellule(TAILLE_GRILLE // 2, TAILLE_GRILLE // 2, 1)
        grille.definir_cellule(TAILLE_GRILLE // 2 + 1, TAILLE_GRILLE // 2, 1)
  
       
    # 3. Initialisation de la Logique du jeu avec la grille
    logic = Logic(grille)

    # 4. Initialisation de l'affichage Pygame
    display_manager = AfficheGrille(grille)
    clock = pygame.time.Clock()

    # --- Boucle principale de simulation et d'affichage ---
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 5. Calcul de la prochaine génération
        nouvelle_grille = logic.CalculerGenerationSuivante()
        logic.grille = nouvelle_grille # Met à jour la grille de la logique avec la nouvelle génération
        display_manager.grille = nouvelle_grille # Met à jour la grille de l'affichage

        # 6. Dessin et mise à jour de l'écran
        display_manager.dessiner_grille_lignes()
        display_manager.dessiner_cellules()
        pygame.display.flip() # Utiliser flip() pour Pygame

        # 7. Contrôle de la vitesse de la simulation
        clock.tick(VITESSE_FPS) # Limite la boucle à VITESSE_FPS images/générations par seconde

    pygame.quit()
    sys.exit()
   
if __name__ == "__main__":
    main()