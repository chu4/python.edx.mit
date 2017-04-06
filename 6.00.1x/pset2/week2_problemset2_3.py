balance=999999
balance1=balance
annualInterestRate=0.18
MonIntRate=annualInterestRate/12.0
MonPayLow=balance/12
MonPayUpp=balance*((1+MonIntRate)**12)/12.0
guessed = False
MonPay= (MonPayUpp+MonPayLow)/2
while not guessed:
    balance1=balance    
    for m in range(12):    
         MonUnBal= balance1-MonPay
         balance1=MonUnBal+MonIntRate*MonUnBal    
    if balance1>0.01:
        MonPayLow=MonPay
        MonPay= (MonPayUpp+MonPayLow)/2        
    elif balance1<-0.01:
        MonPayUpp=MonPay
        MonPay= (MonPayUpp+MonPayLow)/2        
    else:
        guessed=True
print'Lowest Payment:'+str(round(MonPay,2)) 