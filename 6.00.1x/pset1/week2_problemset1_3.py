s = 'smslvpgflmwjgqnenagufom'
res=''
res1=''
for i in range (1,len(s)): 
    if s[i-1]<s[i]:
        res1+=s[i-1] 
        
    elif s[i-1]==s[i]:
        res1+=s[i]
    else:
        res1=res1+s[i-1]
                 
        if len(res)<len(res1):
            res=res1
        res1=''
    
print(res)