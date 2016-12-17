def ff(x):
    a = []
    
    while x > 0:
        a.append(x)
        print a
        f(x-1)
        
class adam(object):
    def __init__(self,a,b):
        sefl.a=a
        self.b=b

        
L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3

def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        iteration += 1
    return lst

def sort2(lst):
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions assume this line just executed
    return lst

def sort3(lst):
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions assume this line just executed
    return out

def sort4(lst):
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])

        L = lst[:]  # the next 3 questions assume this line just executed
        print L
        return unite(front, back)

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    Dict=aDict.copy()
    mDict=aDict.copy()
    if Dict=={}:
        return []
    L=[]
    i=0
    keys=[]
    
    for keyD in Dict.keys():
        for keyaD in mDict.keys():
            if aDict.has_key(keyaD):
                if keyD!=keyaD and Dict[keyD]==mDict[keyaD]:
                    print aDict
                    del aDict[keyaD]
            
   # print Dict
   # print mDict
   # print aDict
     

    for key in aDict.keys():
        if not key in L:
            L.append(key)
    
    L.sort()
    return L
