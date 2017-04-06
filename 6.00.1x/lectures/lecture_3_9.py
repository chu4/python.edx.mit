print("Please think of a number between 0 and 100!")
x = 100
low = 0
high = x
ans = (high + low)/2
print ('Is your secret number '+str(ans)+'?')

n=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while n!='c': 
  if n=='h' or n=='l'or n=='c':     
      if n=='l':
        low = ans
      elif n=='h':
        high = ans 
      ans = (high + low)/2
      print('Is your secret number '+str(ans)+'?')
      n=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  else:
      print 'Sorry, I did not understand your input.'  
      n=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print('Game over. Your secret number was: ' + str(ans))