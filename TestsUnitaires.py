import unittest
import tkinter as tk
from AfficherCartes import AfficherCartes

class TestAfficherCartes(unittest.TestCase):
    def setUp(self):
        # Configurer une fenêtre Tkinter de base pour les tests
        self.root = tk.Tk()

    def tearDown(self):
        # Nettoyer les ressources après chaque test
        self.root.destroy()

    def test_PasDePseudosVides(self):
        # Tester si la liste de pseudonymes contient des valeurs non vides
        cartes_joueurs = [["cartes/cartes_0.svg", "cartes/cartes_1.svg"], ["cartes/cartes_2.svg", "cartes/cartes_3.svg"]]
        backlog = ["Tâche 1", "Tâche 2"]
        pseudonyms = ["Player1", "Player2", "Player3"]  # Ajoutez un pseudonyme vide ici pour le test
        afficher_cartes = AfficherCartes(self.root, cartes_joueurs=cartes_joueurs, backlog=backlog, mode=0, pseudonyms=pseudonyms, step=0, isFirstTry=True, savedValues=[])

        # Vérifier que la liste de pseudonymes ne contient pas de chaînes vides
        self.assertTrue(all(p != "" for p in afficher_cartes.pseudonyms), "La liste de pseudonymes ne doit pas contenir de valeurs vides")

    def test_Mode1SiMoyenne(self):
        # Test if the 'mode' attribute is correctly set to 1 after selecting the "Moyenne" game mode
        cartes_joueurs = [["cartes/cartes_0.svg", "cartes/cartes_1.svg"], ["cartes/cartes_2.svg", "cartes/cartes_3.svg"]]
        backlog = ["Tâche 1", "Tâche 2"]
        pseudonyms = ["Player1", "Player2"]
        
        # Create an instance of AfficherCartes with 'Moyenne' game mode selected
        afficher_cartes = AfficherCartes(self.root, cartes_joueurs=cartes_joueurs, backlog=backlog, mode=1, pseudonyms=pseudonyms, step=0, isFirstTry=True, savedValues=[])

        # Verify that the 'mode' attribute is set to 1
        self.assertEqual(afficher_cartes.mode, 1, "Le mode doit être correctement défini à 1 après la sélection du mode 'Moyenne'")

    def test_Mode0SiStrict(self):
        # Test if the 'mode' attribute is correctly set to 0 after selecting the "Strict" game mode
        cartes_joueurs = [["cartes/cartes_0.svg", "cartes/cartes_1.svg"], ["cartes/cartes_2.svg", "cartes/cartes_3.svg"]]
        backlog = ["Tâche 1", "Tâche 2"]
        pseudonyms = ["Player1", "Player2"]
        
        # Create an instance of AfficherCartes with 'Strict' game mode selected
        afficher_cartes = AfficherCartes(self.root, cartes_joueurs=cartes_joueurs, backlog=backlog, mode=1, pseudonyms=pseudonyms, step=0, isFirstTry=True, savedValues=[])

        # Select 'Strict' game mode
        afficher_cartes.mode = 0

        # Verify that the 'mode' attribute is set to 0
        self.assertEqual(afficher_cartes.mode, 0, "Le mode doit être correctement défini à 0 après la sélection du mode 'Strict'")


if __name__ == '__main__':
    unittest.main()