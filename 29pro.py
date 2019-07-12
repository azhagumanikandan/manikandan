#azhagu
xx = int(input())
tt = int(xx/2)
rr = []
for i in range(xx, tt, -1):
    j = str(i)
    if i + sum([int(kk) for kk in j]) == xx:
        print(1)
        print(i)
        break
else:
    print(0)
