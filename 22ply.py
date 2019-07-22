#azhagu
p,q=map(int,input().split())

for i in range(1,min(p,q)+1):

    if((p%i==0) and (q%i==0)):
    
        x=i
        
print(x)
