#azhagu
x1,y1=map(int,input().split())
mn1=0
L1=[]
for i in range(x1):
      L1.append(input())
for i in range(x1):
      for j in range(y1-1):
            if(L1[i][j]!='R' and L1[i][j+1]!='R'):
                  mn1+=3
            elif(L1[i][j]!='G' and L1[i][j+1]!='G'):
                  mn1+=5
print(mn1)
