def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
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
        print(counter)
        return True
    else:
        print(counter)
        return False