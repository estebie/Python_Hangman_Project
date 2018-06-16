"""

The python module for reading and writing files.

"""

import random

def pick_word():
    """
        Picks a word from the word bank file.
    """
    try:
        with open('hangman_wordbank.txt', 'r') as file:
            words = file.readlines()
            return words[random.randint(0, len(words) - 1)]
    except IOError as error: 
        print('File read error: '+ error)
        return ''

if __name__ == "__main__":
    print(pick_word())
    input()
