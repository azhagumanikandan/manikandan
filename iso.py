    
ak,aks=map(str,input().split())
if(len(akshu)!=len(ak)):
  print("no")
a=[ak.count(j) for j in ak]
b=[aks.count(j) for j in aks]
if a==b:
  print("yes")
else:
  print("no")
