balance=4773
balance1=balance
annualInterestRate=0.2
MonPay=0
pay=0
m=0
MonIntRate=annualInterestRate/12.0
while balance1>0:
    balance1=balance
    MonPay+=10
    for m in range(12):   
         MonUnBal= balance1-MonPay
         balance1=MonUnBal+MonIntRate*MonUnBal   
print'Lowest Payment:'+str(MonPay) 