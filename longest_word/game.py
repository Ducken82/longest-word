"""Module contenant l'implémentation du jeu The Longest Word."""

import random
import string


class Game:
    """Classe représentant le jeu du Longest Word."""

    # pylint: disable=too-few-public-methods

    def __init__(self):
        """Attribue une grille aléatoire de 9 lettres."""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Retourne True si et seulement si le mot est valide selon la grille du jeu."""
        word = word.upper()  # Normaliser le mot en majuscules

        # Vérifier que chaque lettre du mot est bien présente dans la grille
        grid_copy = self.grid[:]  # Faire une copie pour éviter de modifier l'originale
        for letter in word:
            if letter in grid_copy:
                grid_copy.remove(letter)  # Retirer la lettre utilisée
            else:
                return False  # Lettre absente ou en quantité insuffisante

        return True  # Si toutes les lettres sont trouvées dans la grille


if __name__ == "__main__":
    game = Game()
    print("Grille de jeu :", game.grid)
    test_word = input("Entrez un mot : ").upper()
    print(f"Le mot '{test_word}' est valide :", game.is_valid(test_word))
