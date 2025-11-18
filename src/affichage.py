import pygame


class AfficheGrille:

    def __init__(self):
        pygame.init()

        # Fenêtre NON full screen → 900x900
        self.screen = pygame.display.set_mode((900, 900))
        pygame.display.set_caption("Grille 50 x 50")

        # Dimensions
        self.width, self.height = self.screen.get_width(), self.screen.get_height()

        # Couleurs
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Taille de la grille
        self.ligne = 50
        self.colonne = 50

        # Taille d’une cellule
        self.cell_width = self.width // self.colonne
        self.cell_height = self.height // self.ligne

    def dessiner_grille(self):

        self.screen.fill(self.black)

        # Lignes verticales
        for col in range(self.colonne + 1):
            x = col * self.cell_width
            pygame.draw.line(self.screen, self.white, (x, 0), (x, self.height), 1)

        # Lignes horizontales
        for lig in range(self.ligne + 1):
            y = lig * self.cell_height
            pygame.draw.line(self.screen, self.white, (0, y), (self.width, y), 1)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

            self.dessiner_grille()
            pygame.display.update()


if __name__ == "__main__":
    jeu = AfficheGrille()
    jeu.run()
