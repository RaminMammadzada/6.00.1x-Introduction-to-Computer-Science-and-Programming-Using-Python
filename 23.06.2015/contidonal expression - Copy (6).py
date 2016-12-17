x=int(raw_input('Enter the value for x: '))
y=int(raw_input('Enter the value for y: '))
z=int(raw_input('Enter the value for z: '))

if x<y and x<z:
    print('x is least')
elif y<z:
    print('y is least')
else:
    print('z is least')
