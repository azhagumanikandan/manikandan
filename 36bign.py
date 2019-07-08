#azhagu
aa=input()
count=0
for i in range(len(aa)):
  if aa[i].isdigit() or aa[i].isalpha():
    bb=0
  else:
    count+=1
print(count)
