# Hangman Game 🎮

Welcome to the Hangman Game! This is a simple text-based implementation of the classic Hangman game written in Python. The objective is to guess the secret word one letter at a time before you run out of attempts.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Contributing](#contributing)
- [License](#license)

## Description 📄

This Hangman game selects a random word from a predefined list and displays a series of underscores representing the hidden letters of the word. Players must guess the word by suggesting letters within a limited number of attempts. For every incorrect guess, a part of the hangman is drawn. The game ends when the player either correctly guesses the word or the hangman drawing is completed.

## Installation 💻

To run this game, you'll need Python installed on your computer. You can download Python from [python.org](https://www.python.org/).

Clone this repository to your local machine using:
```bash
git clone https://github.com/your-username/hangman-game.git
```

Navigate to the project directory:
```bash
cd hangman-game
```

## Usage ▶️

Run the game script using Python:
```bash
python hangman.py
```

## How to Play 🎲

1. The game will randomly select a secret word from a list of words.
2. The secret word will be represented by underscores `_`.
3. You will be prompted to guess a letter.
4. If the guessed letter is in the secret word, it will be revealed in the correct positions.
5. If the guessed letter is not in the secret word, a part of the hangman will be drawn.
6. Continue guessing letters until you either guess the word correctly or the hangman drawing is complete.
7. If the hangman drawing is complete before you guess the word, the game is over, and you lose.
8. If you guess the word before the hangman drawing is complete, you win!
9. After the game ends, you will be asked if you want to play again.

### Example Output

```
  +---+
  |   |
      |
      |
      |
      |
=========
The secret word:
_____
Missed letters:

Make a guess:
```

### Note

- Input is case-insensitive; both uppercase and lowercase letters are treated as the same.
- Only single letter guesses are allowed.
- If you guess a letter you already guessed, you'll be prompted to try a different letter.


## License ⚖️

Distributed under the MIT License. See `LICENSE` for more information.

---

Replace `your-username` with your actual GitHub username in the clone command, and make sure to include a `LICENSE` file if you want to distribute the project under a specific license.
