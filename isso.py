m,m2=map(str,input().split())
if(len(m)!=len(m)):
  print("no")
a=[m.count(i) for i in n]
b=[m2.count(i) for i in n2]
if a==b:
  print("yes")
else:
  print("no")
