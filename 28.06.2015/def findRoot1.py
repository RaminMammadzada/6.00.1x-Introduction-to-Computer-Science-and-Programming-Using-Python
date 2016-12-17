def findRoot1(x,power,epsilon):
    low=0
    high=x
    ans=(high+low)/2.0
    while abs(ans**power-x)>epsilon:
        if ans**power<x:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
    return ans
