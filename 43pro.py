#azhagu
thi1 = int(input())
aaa1 = list(map(int,input().split()))
ss1,l = 0,[]
bb1 = [x for x in range(1,thi1+1)]
for i in aaa1:
  if i in bb1:
    bb1.remove(i)
kh1 = 0
for i in range(0,thi1-1):
  p1 = aaa1[i]
  for j in range(i+1,thi1):
    if p1 == aaa1[j]:
      if p1 < bb1[kh1]:
        aaa1[j] = bb1[kh1]
        ss1 += 1
      else:
        aaa1[i] = bb1[kh1]
        ss1 += 1
      kh1 += 1
print(ss1)
print(*aaa1)
