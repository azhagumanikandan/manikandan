#azhagu
p1 = int(input())
q1 = [ int(x) for x in input().split()]
p1 = len(q1)
u1 = 0
for i in range(0,p1-2):
    for j in range(i+1, p1-1):
        for k in range(j+1, p1):
            if q1[i] > q1[j] > q1[k] :
                u1 =u1+ 1
print(u1)
