def genFib():
    fibn_1=1 #fib(n-1)
    fibn_2=0 #fib(n-2)
    while True:
        #fib(n)=fib(n-1)+fib(n-2)
        next=fibn_1+fibn_2
        yield next
        fibn_2=fibn_1
        fibn_1=next
        
def genPrimes():
    prime_number=2
    divisor=0
    while True:
        control=0
        divisor=prime_number
        for divis in range(1,divisor+1):
            if (prime_number%divis)==0:
                control+=1
        if control<3:
            yield prime_number
        prime_number+=1
def generator1():
    if True:
        yield 1 

def generator2():
    if False:   
        yield 1

g1 = generator1()
g2 = generator2()

print type(g1)
print type(g2)
print g1.next()
print g2.next()
