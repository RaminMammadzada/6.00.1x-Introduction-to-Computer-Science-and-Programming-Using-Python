# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    # My code
    # -------
    dictionary={} # this is a blank dictionary
    big_letters=string.ascii_uppercase # firstly we need to assign all uppercase letters
    small_letters=string.ascii_lowercase # frstly we need toassign all lowercase letters
    start=0 # this shows the place where the counting will start
    
    for a in big_letters: # we are appending objects to the dictionary by this (for) loop
        dictionary[a]=big_letters[start+shift]
        start+=1
        if start+shift==26: # this includes the exception in the end of the string into account.
            start=0
            shift=0

    for a in small_letters: # we are appending objects to the dictionary by this (for) loop
        dictionary[a]=small_letters[start+shift]
        start+=1
        if start+shift==26: # this includes the exception in the end of the string into account.
            start=0
            shift=0
    #print dictionary
    return dictionary
    # -------
    # My code
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    # My code
    # -------
    coded_text=''
    for a in text:
        if a in string.punctuation or a in string.digits or a==' ' or a=='\n':
            coded_text+=a
        else:
            coded_text+=coder[a]
    return coded_text
    # -------
    # My code
    ### TODO.
    
    
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    # My code
    # -------
    return applyCoder(text, buildCoder(shift))    
    # -------
    # My code
    ### HINT: This is a wrapper function.
    
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    shifted_text: string
    text: string
    returns: 0 <= int < 26
    """
    # My code
    # -------
    real_words=0    # Set the maximum number of real English words
    max_real_words=0
    best_shift=0    # Assign the best sign to 0
    shift=0         # the while loop should turn 26 times in order to check all of the possibilites of finding maxsimum English words in each shift loop
    word=''
    while shift<26:
        shifted_text=applyShift(text,shift)  # Shift the entire text by this shift value
        for a in shifted_text:
            if a!=' ':
                word+=a#
                #print word
            else:
                if isWord(wordList, word):
                    real_words+=1
                    #print '>>>'+ word
                word=''
        
        if real_words>max_real_words:
            max_real_words=real_words
            best_shift=shift
            
        shift+=1
        word=''
        real_words=0
    return best_shift
    # -------
    # My code
    
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    # My code
    # -------
    text=getStoryString()
    wordList=loadWords()
    shift=findBestShift(wordList,text)
    return applyShift(text,shift)
    # -------
    #My code
    
#
# Build data structures used for entire session and run encryption
#
print decryptStory()
    
'''filem=open('encrypted_code.txt','r')
text=filem.read()
print findBestShift(loadWords(),text)'''
