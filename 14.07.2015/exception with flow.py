def getRatios(v1, v2):
    """ Assumes: v1 and v2 are lists of equal lenght of numbers
        Returns a list containing the meaningful values of
        v1[i]/v2[i]"""
    ratios=[]
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) # NaN= Not a Number
        except:
            raise ValueError('getRatios called with bad arg')
    return ratios

def test():
    try:
        print getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0])
        print getRatios([],[])
        print getRatios([1.0,2.0], [3.0])
    except ValueError, msg:
        print msg
    
    
