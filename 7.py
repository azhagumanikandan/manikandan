b=input()
l=[a[i] for i in range(len(b)) if i%2==0]
l1=[b[i] for i in range(len(b)) if i%2!=0]
for j in range(len(b)//2):
  print(l1[j]+l[j],end="")
