#azhagu

n,k,p=map(str,input().split())

n=list(n)

k=list(k)

p=int(p)

count2=0

for i in range(0,len(n)):

        if(n[i]!=k[i]):
        
            count2=count2+1
            
if(count2==p):

    print("yes")
    
else:

    print("no")
