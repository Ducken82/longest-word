"""Module contenant l'implémentation du jeu The Longest Word."""

import random
import string
import requests

class Game:
    """Classe représentant le jeu The Longest Word."""

    # pylint: disable=too-few-public-methods
    def __init__(self):
        """Attribue une grille aléatoire de 9 lettres."""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Retourne True si et seulement si le mot est valide selon la grille du jeu et le dictionnaire."""
        word = word.upper()  # Normaliser le mot en majuscules

        # Vérifier que chaque lettre du mot est bien présente dans la grille
        grid_copy = self.grid[:]  # Faire une copie pour éviter de modifier l'originale
        for letter in word:
            if letter in grid_copy:
                grid_copy.remove(letter)  # Retirer la lettre utilisée
            else:
                return False  # Lettre absente ou en quantité insuffisante

        # Vérifier si le mot existe dans le dictionnaire via l'API
        api_url = f"https://dictionary.lewagon.com/{word.lower()}"
        try:
            response = requests.get(api_url, timeout=5)  # Ajout d'un timeout de 5s
            response.raise_for_status()
            data = response.json()
            return data.get("found", False)  # Vérifier si le mot est reconnu par l'API
        except requests.RequestException:
            return False  # En cas d'erreur de requête, considérer que le mot n'est pas valide
