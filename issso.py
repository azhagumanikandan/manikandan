ai,bi=map(str,input().split())
if(len(ai) != len(bi)):
    print('no')
xx=[ai.count(ch1) for ch1 in ai]
yy=[bi.count(ch1) for ch1 in bi]
if(xx==yy):
    print('yes')
else:
    print('no')
