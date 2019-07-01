aa=int(input())
n=[]
l=[]
n1=[]
for k in range (aa):
    n.append(input())
    
for k in range (0,aa):
    l.append( len(n[k]))
sa=min(l)
if(sa!=1):
    i=0
    for m in range(0,sa):
        if((n[k][m]==n[k+1][m]) ):
            n1.append(n[k][m])
print(*n1,sep='')
