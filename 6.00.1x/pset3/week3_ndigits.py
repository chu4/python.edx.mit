x=100
def ndigits(x):
   n=1
   if x/10>=1:
      print n        
   else:
      x=x/10
      n+=1
      return ndigits(x)