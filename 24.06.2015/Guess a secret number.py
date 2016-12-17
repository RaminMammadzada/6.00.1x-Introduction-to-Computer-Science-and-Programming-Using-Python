print('Please think of a number between o and 100!')
high=100
low=0
secret_number=0
while(True):
    
    secret_number=((high+low)/2)
    print('Is your secret number ' + str(secret_number))
    ans=str(raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guess correctly.'))
    if ans=='h':
        high=secret_number
    elif ans=='l':
        low=secret_number    
    elif ans=='c':
        print('Game over. Your secret number was: '+ str(secret_number))
        break
