balance=4213.0
annualInterestRate=0.2
monthlyPaymentRate=0.04

print 'balance: ' + str(balance)
print 'annualInterestRate: ' + str(annualInterestRate)
print 'monthlyPaymentRate: ' + str(monthlyPaymentRate)


month=1
totalPaid=0.0
monthlyPayment=0.0
newbalance=0.0
unpaidBalance=0.0
while month<=12:
    
    print 'Month: ' + str(month)
    monthlyPayment=balance*monthlyPaymentRate
    totalPaid=totalPaid+monthlyPayment
    
    round(monthlyPayment,2)
    
    print 'Minimum monthly payment: ' + str(monthlyPayment)
    

    
    unpaidBalance=balance-monthlyPayment
    newBalance=unpaidBalance+unpaidBalance*annualInterestRate/12.0
    round(newBalance,2)
    
    print 'Remaining balance: ' + str(newBalance)

    
    month=month+1
    balance=newBalance
    
print 'Total paid: ' +  str(totalPaid)
print 'Remaining balance: ' + str(balance)
