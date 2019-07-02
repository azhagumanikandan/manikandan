h=int(input())
y=list(map(int,input().split()))
n=0
for c in range(len(y)-2):
   for f in range(c+1,len(y)-1):
         for e in range(f+1,len(y)):
            if y[c]<y[d]<y[e] and c<f<e:
                n+=1
print(n) 
