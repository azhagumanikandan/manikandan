aa = int(input())
bb = list(map(int,input().split()))
dd = []
for i in bb:
  cc = bin(i)
  dd.append(cc)
ee = sorted(dd)
ee.reverse()
for i in ee:
  print(int(i,2))
