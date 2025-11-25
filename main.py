from src.grille import Grille

grille = Grille(5, 5)

# Active quelques cellules pour faire un Blinker
grille.definir_cellule(1, 2, 1)
grille.definir_cellule(2, 2, 1)
grille.definir_cellule(3, 2, 1)

# Affiche pour vérifier
for ligne in grille.cellules:
    print(ligne)
'''

**Résultat attendu :**
'''
[0, 0, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 0, 0]