#azhagu
n1 = int(input())
power = list(map(int,input().split()))
countt1 = 0
for i in range(len1(power)-2):
    for j in range(i+1,len1(power)-1):
        for k in range(j+1,len1(power)):
            if power[i] > power[j]:
                if power[j] > power[k]:
                    countt1 += 1

print(countt1)
