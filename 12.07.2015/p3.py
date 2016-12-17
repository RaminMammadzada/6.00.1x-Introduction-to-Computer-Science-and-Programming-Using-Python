def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string='abcdefghijklmnopqrstuvwxyz'
    alpha=''
    for guess in lettersGuessed:        
        alpha=string
        string=''
        for letter in alpha:
            if letter!=guess:
                string+=letter
        
    return string