"""

The python module for hangman utilities.

"""

import random, os
from string import ascii_letters

HANGMANPICS = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def game_screen(hangmanIndex, guessedWord):
    """ Prints the gamescreen of the game

    Parameters
    -------------
    hangmanIndex: int, the number of mistakes of the player
    guessedWord : string, a series of underscores that hides the current word

    Returns
    ---------
    void
    
    """
    cls()
    print(HANGMANPICS[hangmanIndex])
    print(*guessedWord)

def pick_word():
    """ Picks a random word from wordbank.txt

    Parameters
    -------------
    None
    
    Returns
    ---------
    randomWord : string, the random word from the word bank 
    """
    randomWord = ''
    try:
        with open('hangman_wordbank.txt', 'r') as file:
            words = file.readlines()
            randomWord = words[random.randint(0, len(words) - 1)]
    except IOError as error: 
        print('File read error: '+ error)

    return randomWord

def generate_dash(word):
    """ Generate dash to hide the word

    Parameters
    -------------
    word : string, the current word in play

    Returns
    ---------
    guessedWord : string, a series of underscores that hides the current word
    """
    guessedWord = list('_' * (len(word) - 1))
    return guessedWord

def check_letter(word, guessedWord, guessedLetter):
    """ Checks a letter in the guessed word if the correct guess is inputted

    Parameters
    -------------
    word : string, the current word in play
    guessedWord : string, a series of underscores that hides the current word
    guessedLetter, char, the user input for guessing the word in the game
    
    Returns
    ---------
    guessFlag : boolean, the boolean value in checking if the inputted character can
        be found in the current word. 
    """
    guessFlag = False

    if (guessedLetter in word):
        for index, letter in enumerate(word):
            if (letter == guessedLetter):
                guessedWord[index] = letter
        guessFlag = True

    return guessFlag

def reveal_letter(word, guessedWord):
    """ Reveals a letter from the guessed word when the guessed character is correct

    Parameters
    -------------
    word : string, the current word in play
    guessedWord : string, a series of underscores that hides the current word

    Returns
    ---------
    tries: int, the number of tries that it took guessing the word.
    """
    tries = 0

    while ('_' in guessedWord):
        guessedLetter = input("Input a letter: ")
        if (check_char(guessedLetter)):
            flag = check_letter(word, guessedWord, guessedLetter)
            
            if (not flag):
                print("Error!")
            else:
                print(*guessedWord)
            tries = tries + 1
        else:
            print("Error! Please enter a letter")
            print(*guessedWord)

    return tries

def check_char(letter):
    """ Check if the letter is a letter

    Parameters
    -------------
    letter: char, input from the user

    Returns
    ---------
    isLetter: boolean, the flag for checking if the input is a letter
    """
    isAlphabet = letter in set(ascii_letters)
    return isAlphabet

if __name__ == "__main__":
    #print(pick_word())
    word = pick_word()
    print(word)
    guessedWord = generate_dash(word)
    print(*guessedWord)
    tries = reveal_letter(word, guessedWord)
    print("It took ", tries, " tries")
    input()
