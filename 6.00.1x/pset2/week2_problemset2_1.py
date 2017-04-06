balance=4842
annualInterestRate=0.2
monthlyPaymentRate=0.04
pay=0
m=0
MonIntRate=annualInterestRate/12.0
while m < 12 :
     m+=1
     MinMonPay= monthlyPaymentRate * balance
     MonUnBal= balance-MinMonPay
     balance=MonUnBal+MonIntRate*MonUnBal
     pay+=MinMonPay
     print 'Month:' +str(m)
     print 'Minimum monthly payment:'+str(round(MinMonPay,2))
     print 'Remaining balance:'+str(round(balance,2))
print 'Total paid:'+str(round(pay,2))
print 'Remaining balance:'+str(round(balance,2))