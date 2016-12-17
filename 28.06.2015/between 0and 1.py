def findRoot2(x,power,epsilon):

    low=min(0,x)
    high=max(0,x)
    ans=(high+low)/2.0


    while abs(ans**power-x)>epsilon:
        if ans**power<x:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
    return ans
