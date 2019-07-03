#azhagu
nn1,k1=map(int,input().split())
ain1= [[abs(i-k),i]for i in [int(x) for x in input().split()]]
ain1.sort()
ain1=ain1[1:]
ain1=[i[1] for i in ain1[:3]]
print(*ain1)
