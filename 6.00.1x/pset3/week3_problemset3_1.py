def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
start=40
stop=100
step=1.5
n=0.0
i=start
while i < stop:
    
    k=f(i)*step
    n+=k
    i+=step
    
print n