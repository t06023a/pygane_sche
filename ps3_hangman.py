# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    # FILL IN YOUR CODE HERE...
    for x in secretWord:
        if x not in lettersGuessed:
            return False

    return True





def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    x = len(secretWord)
    y1 = '_'
    y = [y1]
    wr =  x * y
    j=-1
    for i in secretWord:
        j += 1
        if i in lettersGuessed:

            wr[j] = i
    ret = ''
    for i in wr :
        ret = ret + i

    return ret


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    ava = ''
    lett  = string.ascii_lowercase
    for i in lett :
        if i not in lettersGuessed:
            ava = ava + i
    return ava

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
    # FILL IN YOUR CODE HERE...
    print('Welcome  to the game, Hangman!')

    print('I am thinking of a word  that is ' + str(len(secretWord))    + ' letters long.')
    x = 0
    y = 8

    global lettersGuessed
    lettersGuessed =  []
    
    lserstwword = len(secretWord)

    swordl = lserstwword*'_'

    y = 8
    while y > 0:

        print('------------')

        x = x+1

        print ('You have', y ,'guesses left.')

        current  = getAvailableLetters(lettersGuessed)
        current = current.lower()

        print ("Available letters: " , current)
        guees = input("Please guess a letter:"   )
        guees = guees.lower()

        if guees in  lettersGuessed :
            x1 = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: " + x1)
            continue
        else :
            lettersGuessed+=  guees
        if guees in secretWord :
            gw = getGuessedWord(secretWord, lettersGuessed)
            print ("Good guess: ",  gw)
        else :
            gw = getGuessedWord(secretWord, lettersGuessed)
            print ('Oops! That letter is not in my word:',gw)
            y = y -1
        if isWordGuessed(secretWord, lettersGuessed):
            print('')
            print('------------')
            print('')
            print('Congratulations, you won!')
            return
            y = 0
    print('')
    print('------------')
    print('')
    print ('Sorry, you ran out of guesses. The word was ' +  secretWord + '.')
    return




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print (secretWord)
hangman('c')


