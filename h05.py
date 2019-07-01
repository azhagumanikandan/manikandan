m=str(input())
e=1
for i in range(len(m)-1):
    a=int(m[i]+m[i+1])
    if(a<=26 and m[i]!="0"):
        d=d+1
if(e==3):        
    print(e)
else:
    print(e+(e-1)//2) 
