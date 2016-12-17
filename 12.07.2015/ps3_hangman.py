# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    #My code:
    #---------
    counter=0
    if len(secretWord)==0 and len(lettersGuessed)==0:
        return True
    else:
        for guess in lettersGuessed:
            for secret in secretWord:
                if guess==secret:
                    counter+=1
                    break
        
    
    if counter==len(secretWord):
        return True
    else:
        return False
    #--------
    #My code




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #My code:
    #---------

    string=''
    for a in range(len(secretWord)):
        string+=str(a)
    
    i=0
    while i<len(secretWord):
        b=str(i)
        for guess in lettersGuessed:
            if guess==secretWord[i]:
                string=string.replace(str(i),guess)
        if b==str(i):
            string=string.replace(str(i),'_')
                
        i+=1
                
    return string
    
    #--------
    #My code

def lettersInGuess(secretWord,inp):
    #My code:
    #---------

    control=0
    for a in secretWord:
        if inp==a:
            control+=1
    if control!=0:
        return True
    else:
        return False
    #--------
    #My code



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #My code:
    #---------
    string='abcdefghijklmnopqrstuvwxyz'
    alpha=''
    for guess in lettersGuessed:        
        alpha=string
        string=''
        for letter in alpha:
            if letter!=guess:
                string+=letter
        
    return string
    #--------
    #My code    

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
    print 'Welcome to the game, Hangman!'
    
    print 'I am thinking of a word that is ' + str(len(secretWord))+ ' letters long.'
    guess=8
    lettersGuessed=''
    control=''
    inp=''
    while guess>0:
        print 'You have ' + str(guess) + ' guesses left.'
        
        print 'Available letters: '+ getAvailableLetters(lettersGuessed)
        while(inp==control):
            inp=raw_input('Please guess a letter: ')
        
        control=inp
        inp=inp.lower()
        lettersGuessed+=inp

        
        
        if lettersInGuess(secretWord,inp)==True:        
            print 'Good guess: '+ getGuessedWord(secretWord, lettersGuessed)
        else:
            print 'ops! That letter is not in my word: ' +getGuessedWord(secretWord, lettersGuessed)
        
        if isWordGuessed(secretWord, lettersGuessed)==True:
            print 'Congratulations, you won!'
            break
        
        print ''
        print '-----------------'
        print ''
        
        guess-=1

        if guess==0:
           print ' Sorry, you ran out of guesses. The word was else.'
    print 'The secret word was ' + str(secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
