"""

The main program for the mini-game

"""

import HangmanUtilities

if __name__ == '__main__':
    guessCount = 0
    hangmanIndex = 0
    winFlag = False

    word = list(HangmanUtilities.pick_word().strip().upper())
    guessedWord = list('_' * len(word))
    guessedLetters = []

    while(guessCount < 6):
        HangmanUtilities.game_screen(hangmanIndex, guessedWord)
        guessedLetter = input("Input a letter: ").upper()
        flag = HangmanUtilities.check_letter(word, guessedWord, guessedLetter)

        if (not flag):
            if (guessedLetter not in guessedLetters):
                guessedLetters.append(guessedLetter)
                hangmanIndex = hangmanIndex + 1

        guessCount = guessCount + 1
        
        if ('_' not in guessedWord):
            HangmanUtilities.game_screen(hangmanIndex, guessedWord)
            print("You guessed the word!")
            winFlag = True
            break

    if (not winFlag):
        HangmanUtilities.game_screen(hangmanIndex, guessedWord)
        print("You lost!")
    input()