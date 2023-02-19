# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(lettersGuessed) & set(secretWord) == set(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_ '

    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join([letter for letter in string.ascii_lowercase if letter not in lettersGuessed])


def checkLetter(letter, lettersGuessed, numberOfChance, secretWord):
    separator = '-------------'
    if letter not in secretWord and letter not in lettersGuessed:
        numberOfChance -= 1
        lettersGuessed.append(letter)
        print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
        print(separator)
    elif letter not in lettersGuessed:
        lettersGuessed.append(letter)
        print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        print(separator)
    else:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        print(separator)
    return numberOfChance


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')

    numberOfChance = 8
    lettersGuessed = []
    while numberOfChance > 0:
        print('You have', numberOfChance, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        letterGuess = input('Please guess a letter: ')
        letter = letterGuess.lower()

        numberOfChance = checkLetter(letter, lettersGuessed, numberOfChance, secretWord)

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            return

    print('Sorry, you ran out of guesses. The word was else. ')
    return


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
