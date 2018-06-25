"""

The main program for the mini-game

"""

import HangmanUtilities

if __name__ == "__main__":
    word = HangmanUtilities.pick_word()
    guessedWord = HangmanUtilities.generate_dash(word)
    
    HangmanUtilities.game_screen(0, guessedWord)
    input()