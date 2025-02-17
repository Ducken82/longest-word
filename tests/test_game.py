import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from longest_word.game import Game

class TestGame:
    def test_is_valid(self):
        # Setup
        game = Game()
        game.grid = ["B", "A", "R", "O", "Q", "U", "E", "Z", "W"]  # Grille fixe

        # Exercise & Verify
        assert game.is_valid("BAROQUE") is True  # Mot présent dans la grille
        assert game.is_valid("BOWER") is True  # Autre mot valide
        assert game.is_valid("HOUSE") is False  # Contient des lettres absentes de la grille
