import pygame
import sys
from .grille import Grille


class AfficheGrille:

    def __init__(self, grille: Grille):
        pygame.init()
        
        # 1. Intégration de l'objet Grille
        self.grille = grille
        
        # Dimensions de la grille (lignes/colonnes)
        self.lignes, self.colonnes = self.grille.obtenir_dimensions()

        # Fenêtre fixe 900x900
        self.width, self.height = 900, 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"Jeu de la Vie - {self.lignes} x {self.colonnes}")

        # Couleurs
        self.couleur_ligne = (255, 255, 255) # Blanc pour les lignes de grille
        self.couleur_morte = (0, 0, 0)      # Noir pour les cellules mortes
        self.couleur_vivante = (255, 255, 255) # Blanc pour les cellules vivantes

        # Taille d’une cellule
        self.cell_width = self.width // self.colonnes
        self.cell_height = self.height // self.lignes

    def dessiner_cellules(self):
        
        # 2. Dessiner l'état des cellules
        for i in range(self.lignes):
            for j in range(self.colonnes):
                
                etat = self.grille.obtenir_cellule(i, j)
                
                if etat == 1:
                    # Coordonnées et dimensions du carré à dessiner
                    x = j * self.cell_width
                    y = i * self.cell_height
                    rect = pygame.Rect(x + 1, y + 1, self.cell_width - 1, self.cell_height - 1)
                    
                    # Dessine le carré blanc pour une cellule vivante
                    pygame.draw.rect(self.screen, self.couleur_vivante, rect)
                else:
                    # Dessine le carré noir pour une cellule morte (remplissage initial)
                    x = j * self.cell_width
                    y = i * self.cell_height
                    rect = pygame.Rect(x + 1, y + 1, self.cell_width - 1, self.cell_height - 1)
                    pygame.draw.rect(self.screen, self.couleur_morte, rect)


    def dessiner_grille_lignes(self):
        
        # Remplissage initial de l'écran avec la couleur des cellules mortes
        self.screen.fill(self.couleur_morte)

        # Lignes verticales
        for col in range(self.colonnes + 1):
            x = col * self.cell_width
            pygame.draw.line(self.screen, self.couleur_ligne, (x, 0), (x, self.height), 1)

        # Lignes horizontales
        for lig in range(self.lignes + 1):
            y = lig * self.cell_height
            pygame.draw.line(self.screen, self.couleur_ligne, (0, y), (self.width, y), 1)


    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # Ordre de dessin : d'abord les lignes de la grille, puis l'état des cellules
            self.dessiner_grille_lignes()
            self.dessiner_cellules()
            
            pygame.display.update()

if __name__ == "__main__":
    
    jeu = AfficheGrille(Grille (50, 50))
    jeu.run()