# wsgi.py

# pylint: disable=missing-docstring

from flask import Flask, render_template, request
from longest_word.game import Game

app = Flask(__name__)

@app.route('/')
def home():
    """
    Route principale qui affiche la grille de lettres et permet à l'utilisateur
    d'entrer un mot pour le valider.
    """
    game = Game()
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    """
    Route qui reçoit un mot soumis par l'utilisateur et vérifie s'il est valide
    par rapport à la grille et au dictionnaire.
    """
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
