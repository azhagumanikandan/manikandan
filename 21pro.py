#azhagu
pqq=int(input())
rss=list(map(int,input().split()))
avg=int(pqq/2)
laa=rss[:avg]
lb=rss[avg::]
if ((sum(laa)//len(laa))==(sum(lb)//len(lb))):
    print("yes")
else:
    print("no")
