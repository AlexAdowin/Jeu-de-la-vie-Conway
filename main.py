from src.grille import Grille

# Crée une petite grille pour tester
grille = Grille(3, 4)

# Affiche-la pour vérifier
for ligne in grille.cellules:
    print(ligne)

print(f"Dimensions : {grille.lignes} x {grille.colonnes}")

'''Résultat attendu :
```
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
Dimensions : 3 x 4'''