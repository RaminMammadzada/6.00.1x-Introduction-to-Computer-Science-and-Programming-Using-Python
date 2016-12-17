sentence='I will be one of the best programmers and robot specialists'
doc=open('ramin.txt','a')
doc.write(sentence)
int=int(raw_input('please enter an integer: '))
if int>10:
    doc.write('\n\n')
    doc.write('the value of the integer is bigger than "10"')
elif int==10:
    doc.write('\n\n')
    doc.write('the value of the integer is equal to "10"')
else:
    doc.write('\n\n')
    doc.write('the vaule of the integer is less than "10"')
doc.close()
