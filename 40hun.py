#azhagu
N1 = input()
b1 = []
for i in N1:
  b1.append(int(i))
cc = str(sum(b1))
if(cc == cc[::-1]):
  print("YES")
else:
  print("NO")
