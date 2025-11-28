import unittest
import os
import tempfile
from src.grille import Grille


class TestGrille(unittest.TestCase):
    
    def setUp(self):
        """Préparation avant chaque test"""
        self.grille = Grille(10, 10)
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        self.grille = None
    
    # ========== TESTS D'INITIALISATION ==========
    
    def test_initialisation_grille(self):
        """Test que la grille est correctement initialisée"""
        grille = Grille(5, 8)
        self.assertEqual(grille.lignes, 5)
        self.assertEqual(grille.colonnes, 8)
        self.assertEqual(len(grille.cellules), 5)
        self.assertEqual(len(grille.cellules[0]), 8)
    
    def test_cellules_initialement_mortes(self):
        """Test que toutes les cellules sont mortes (0) à l'initialisation"""
        for ligne in self.grille.cellules:
            for cellule in ligne:
                self.assertEqual(cellule, 0)
    
    # ========== TESTS OBTENIR_CELLULE ==========
    
    def test_obtenir_cellule_valide(self):
        """Test l'obtention d'une cellule avec des coordonnées valides"""
        self.grille.cellules[3][4] = 1
        self.assertEqual(self.grille.obtenir_cellule(3, 4), 1)
    
    def test_obtenir_cellule_coin_superieur_gauche(self):
        """Test l'obtention de la cellule en haut à gauche"""
        self.assertEqual(self.grille.obtenir_cellule(0, 0), 0)
    
    def test_obtenir_cellule_coin_inferieur_droit(self):
        """Test l'obtention de la cellule en bas à droite"""
        self.assertEqual(self.grille.obtenir_cellule(9, 9), 0)
    
    def test_obtenir_cellule_ligne_negative(self):
        """Test qu'une IndexError est levée pour une ligne négative"""
        with self.assertRaises(IndexError):
            self.grille.obtenir_cellule(-1, 5)
    
    def test_obtenir_cellule_colonne_negative(self):
        """Test qu'une IndexError est levée pour une colonne négative"""
        with self.assertRaises(IndexError):
            self.grille.obtenir_cellule(5, -1)
    
    def test_obtenir_cellule_ligne_hors_limite(self):
        """Test qu'une IndexError est levée pour une ligne hors limites"""
        with self.assertRaises(IndexError):
            self.grille.obtenir_cellule(10, 5)
    
    def test_obtenir_cellule_colonne_hors_limite(self):
        """Test qu'une IndexError est levée pour une colonne hors limites"""
        with self.assertRaises(IndexError):
            self.grille.obtenir_cellule(5, 10)
    
    # ========== TESTS DEFINIR_CELLULE ==========
    
    def test_definir_cellule_vivante(self):
        """Test la définition d'une cellule comme vivante (1)"""
        self.grille.definir_cellule(5, 5, 1)
        self.assertEqual(self.grille.cellules[5][5], 1)
    
    def test_definir_cellule_morte(self):
        """Test la définition d'une cellule comme morte (0)"""
        self.grille.cellules[5][5] = 1
        self.grille.definir_cellule(5, 5, 0)
        self.assertEqual(self.grille.cellules[5][5], 0)
    
    def test_definir_cellule_etat_invalide(self):
        """Test qu'une ValueError est levée pour un état invalide"""
        with self.assertRaises(ValueError):
            self.grille.definir_cellule(5, 5, 2)
        
        with self.assertRaises(ValueError):
            self.grille.definir_cellule(5, 5, -1)
    
    def test_definir_cellule_ligne_negative(self):
        """Test qu'une IndexError est levée pour une ligne négative"""
        with self.assertRaises(IndexError):
            self.grille.definir_cellule(-1, 5, 1)
    
    def test_definir_cellule_colonne_negative(self):
        """Test qu'une IndexError est levée pour une colonne négative"""
        with self.assertRaises(IndexError):
            self.grille.definir_cellule(5, -1, 1)
    
    def test_definir_cellule_ligne_hors_limite(self):
        """Test qu'une IndexError est levée pour une ligne hors limites"""
        with self.assertRaises(IndexError):
            self.grille.definir_cellule(10, 5, 1)
    
    def test_definir_cellule_colonne_hors_limite(self):
        """Test qu'une IndexError est levée pour une colonne hors limites"""
        with self.assertRaises(IndexError):
            self.grille.definir_cellule(5, 10, 1)
    
    # ========== TESTS OBTENIR_DIMENSIONS ==========
    
    def test_obtenir_dimensions(self):
        """Test l'obtention des dimensions de la grille"""
        lignes, colonnes = self.grille.obtenir_dimensions()
        self.assertEqual(lignes, 10)
        self.assertEqual(colonnes, 10)
    
    def test_obtenir_dimensions_grille_non_carree(self):
        """Test l'obtention des dimensions d'une grille non carrée"""
        grille = Grille(7, 15)
        lignes, colonnes = grille.obtenir_dimensions()
        self.assertEqual(lignes, 7)
        self.assertEqual(colonnes, 15)
    
    # ========== TESTS REINTIALISER_GRILLE ==========
    
    def test_reinitialiser_grille(self):
        """Test que la réinitialisation remet toutes les cellules à 0"""
        # Définir quelques cellules vivantes
        self.grille.definir_cellule(2, 3, 1)
        self.grille.definir_cellule(5, 7, 1)
        self.grille.definir_cellule(8, 9, 1)
        
        # Réinitialiser
        self.grille.reintialiser_grille()
        
        # Vérifier que toutes les cellules sont mortes
        for ligne in self.grille.cellules:
            for cellule in ligne:
                self.assertEqual(cellule, 0)
    
    def test_reinitialiser_grille_conserve_dimensions(self):
        """Test que la réinitialisation conserve les dimensions"""
        self.grille.reintialiser_grille()
        lignes, colonnes = self.grille.obtenir_dimensions()
        self.assertEqual(lignes, 10)
        self.assertEqual(colonnes, 10)
    
    # ========== TESTS CHARGER_DEPUIS_FICHIER ==========
    
    def test_charger_fichier_valide(self):
        """Test le chargement d'un fichier valide"""
        # Créer un fichier temporaire
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("0 1 0\n")
            f.write("1 1 1\n")
            f.write("0 0 1\n")
            fichier_temp = f.name
        
        try:
            grille = Grille(3, 3)
            grille.charger_depuis_fichier(fichier_temp)
            
            # Vérifier le contenu
            self.assertEqual(grille.cellules[0][0], 0)
            self.assertEqual(grille.cellules[0][1], 1)
            self.assertEqual(grille.cellules[0][2], 0)
            self.assertEqual(grille.cellules[1][0], 1)
            self.assertEqual(grille.cellules[1][1], 1)
            self.assertEqual(grille.cellules[1][2], 1)
            self.assertEqual(grille.cellules[2][0], 0)
            self.assertEqual(grille.cellules[2][1], 0)
            self.assertEqual(grille.cellules[2][2], 1)
        finally:
            os.unlink(fichier_temp)
    
    def test_charger_fichier_inexistant(self):
        """Test le chargement d'un fichier inexistant"""
        with self.assertRaises(SystemExit):
            self.grille.charger_depuis_fichier("fichier_inexistant.txt")
    
    def test_charger_fichier_valeurs_invalides(self):
        """Test le chargement d'un fichier avec des valeurs invalides"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("0 1 0\n")
            f.write("1 2 1\n")  # 2 est invalide
            f.write("0 0 1\n")
            fichier_temp = f.name
        
        try:
            with self.assertRaises(SystemExit):
                self.grille.charger_depuis_fichier(fichier_temp)
        finally:
            os.unlink(fichier_temp)
    
    def test_charger_fichier_non_numerique(self):
        """Test le chargement d'un fichier avec des valeurs non numériques"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("0 1 0\n")
            f.write("1 X 1\n")  # X est non numérique
            f.write("0 0 1\n")
            fichier_temp = f.name
        
        try:
            with self.assertRaises(SystemExit):
                self.grille.charger_depuis_fichier(fichier_temp)
        finally:
            os.unlink(fichier_temp)
    
    def test_charger_fichier_plus_grand_que_grille(self):
        """Test le chargement d'un fichier plus grand que la grille"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("0 1 0 1 1\n")
            f.write("1 1 1 0 0\n")
            f.write("0 0 1 1 0\n")
            fichier_temp = f.name
        
        try:
            grille = Grille(2, 3)
            grille.charger_depuis_fichier(fichier_temp)
            
            # Vérifier que seules les 2 premières lignes et 3 premières colonnes sont chargées
            self.assertEqual(grille.cellules[0][0], 0)
            self.assertEqual(grille.cellules[0][1], 1)
            self.assertEqual(grille.cellules[0][2], 0)
            self.assertEqual(grille.cellules[1][0], 1)
            self.assertEqual(grille.cellules[1][1], 1)
            self.assertEqual(grille.cellules[1][2], 1)
        finally:
            os.unlink(fichier_temp)
    
    def test_charger_fichier_lignes_vides(self):
        """Test le chargement d'un fichier avec des lignes vides"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("0 1 0\n")
            f.write("\n")
            f.write("0 0 1\n")
            fichier_temp = f.name
        
        try:
            grille = Grille(3, 3)
            grille.charger_depuis_fichier(fichier_temp)
            
            # La ligne vide ne doit pas causer d'erreur
            self.assertEqual(grille.cellules[0][0], 0)
            self.assertEqual(grille.cellules[0][1], 1)
            self.assertEqual(grille.cellules[0][2], 0)
        finally:
            os.unlink(fichier_temp)


if __name__ == '__main__':
    # Exécuter les tests avec un niveau de verbosité élevé
    unittest.main(verbosity=2)