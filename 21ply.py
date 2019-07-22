#azhagu
x,y=list(map(int,input().split()))

i,j=list(map(int,input().split()))

k,l=list(map(int,input().split()))

if (x==i==k) or (y==j==l) or (x==y) or (i==j) or (k==l) :

    print("yes")
    
else:

    print("no")
