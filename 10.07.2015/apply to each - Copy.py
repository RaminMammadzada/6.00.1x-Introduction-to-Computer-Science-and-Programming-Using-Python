aDict={ 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati','donkey','dog','dingo']}
'''
def applyFuns(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])
        
        
applyFuns(testList, abs)
print(testList)'''

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values=aDict.values()
    i=0
    total=0
    loop=len(aDict)
    while i<loop:
        total+=len(values[i])
        i+=1
    return total
