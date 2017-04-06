s = 'azcbobobegghakl'
n=0
i='bob'
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        n+=1
print n
        
        