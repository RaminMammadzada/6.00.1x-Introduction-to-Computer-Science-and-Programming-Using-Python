s='azcbobobobobobegghakl'
lentgh=len(s)
word=''
char2=''
char3=''
counter=0
for char1 in s:
    word= char1 + char2 + char3
    
    if word=='bob':
        counter+=1
        
    char3=char2
    char2=char1
    
print ('Number of times bob occurs is: ')
print (counter)
