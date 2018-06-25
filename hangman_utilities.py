"""

The python module for hangman utilities.

"""

import random

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


if __name__ == "__main__":
    #print(pick_word())
    word = pick_word()
    print(word)
    guessedWord = generate_dash(word)
    print(*guessedWord)
    while ('_' in guessedWord):
        guessedLetter = input("Input a letter: ")
        flag = check_letter(word, guessedWord, guessedLetter)
		
        if (not flag):
            print("Error!")
        else:
            print(*guessedWord)

    input()
