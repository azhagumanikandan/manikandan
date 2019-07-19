#azhagu

e=list(map(str,input().split()))

o=len(e[0])

t=0

for k in range(o):

    if(e[0][k]!=e[1][k]):
    
        t+=1
        
if(t==1):

    print("yes")
   
else:

    print("no")
