#azhagu

ans=int(input())

word=list(map(str,input().split()[:ans]))

word.sort()


word.sort(key=len)

for i in word:

    print(i,end=" ")
