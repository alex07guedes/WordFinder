# 🟩 Word Finder

## 📌 **Description**
    Word Finder is a word-guessing game inspired by Wordle from The New York Times. 
    The goal of the game is to guess a randomly chosen five-letter word within five attempts. 
    The game provides visual feedback for each attempt by changing the color of the letter tiles to indicate accuracy.

## 📌 **Functionality**
    Generates a random 5-letter word for each game.
    The player can enter words and receive feedback with colors:
    🟩 Green: Correct letter in the correct position.
    🟨 Yellow: Letter is in the word but in the wrong position.
    ⬜ Gray: Letter is not in the word.
    Validates real words using an English dictionary.
    Interactive interface with HTML, CSS, and Flask (Python).
    Stores attempts in the session to keep track of the player's progress.

## 🛠️ **Instalation**

To run the game locally, follow these steps:

1. Install dependencies

Make sure you have Python installed on your system. Then, install the required packages:
    py -m pip install flask
    py -m pip install flask_session
    py -m pip install tempfile
    py -m pip install random_word
    py -m pip install colorama
    py -m pip install pyenchant

2. Run the application

Start the Flask server with the following command:
    py -m flask run

The game will be accessible in your web browser at http://127.0.0.1:5000/.



