def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string=''
    for a in range(len(secretWord)):
        string+='_'
        
    i=0
    while i<len(secretWord):
        for guess in lettersGuessed:
            if guess==secretWord[i]:
                string[i]=guess
                i+=1
                
    return string

----------
    string=''
    control=0
    for guess in lettersGuessed:
        for secret in secretWord:
            
            if guess==secret:
                string+=guess
                control=1
            else:
                if control is 1:
                    string+='_'
                    control=0
                   
    return string      