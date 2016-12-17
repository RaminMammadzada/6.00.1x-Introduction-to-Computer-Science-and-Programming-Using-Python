x=int(raw_input('input the ingeter number which you want to calculate its square root: '))
epsilon=0.01
step=0.5
numGuesses=0
ans=0.0

while(abs(ans**2-x))>=epsilon and ans<=x:
    ans+=step
    numGuesses +=1

print('numGuesses= '+ str(numGuesses))

if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the swuare root of the ' + str(x))