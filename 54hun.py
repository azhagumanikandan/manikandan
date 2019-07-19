#azhagu
nn=int(input())

li1=list(map(int,input().split()))

li2=[]

for i in range(0,nn):

    li2.append(li1[i])
    
    print(min(li2),end=" ")
