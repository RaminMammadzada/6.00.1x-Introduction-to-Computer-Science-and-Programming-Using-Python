#Find the cube root of a perfect cube
x=int(raw_input('Emter an integer'))
ans=0
while ans**3<abs(x):
    ans=ans+1
    print (ans)
if ans**3!=abs(x):
    print( str(x) + ' is not a perfect cube')
else:
    if x<0:
        ans=-ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
    

