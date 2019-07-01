input1=input()
l1=[input1[i] for i in range(len(input1)) if i%2==0]
m1=[input1[i] for i in range(len(input1)) if i%2!=0]
for j in range(len(input1)//2):
  print(m1[j]+l1[j],end="")
