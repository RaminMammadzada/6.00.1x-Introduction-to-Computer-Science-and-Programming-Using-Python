'''
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
'''

'''
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
'''

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    res=1
    counter=0
    while 1:
        res*=b
        if res<=x:
            counter+=1
        else:
            break
    
    return counter

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    listA=[]
    for word in aList:
        counter=0
        for letter in word:
            counter+=1
        if counter<4:
            listA.append(word)
    return listA

def sumDigits(N):
    '''
    N: a non-negative integer
    '''

    if (N/10)==0:
        return N
    else:
        return (N%10) + sumDigits(N/10)

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    listA=[]
    listB=[]
    listA=aDict.keys()

    if len(aDict.values())==0:
        return []
    
    for key in listA:
        if aDict[key]==target:
            listB.append(key)
    listB.sort()
    return listB
    
