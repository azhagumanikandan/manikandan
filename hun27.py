#azhagu
ss=input()
nn=len(ss)

def check_palindrome(ss,nn):
    if ss==ss[-1:-nn-1:-1]:
        nn-=1
        ss=ss[0:nn]
        check_palindrome(ss,nn)
    else:
        print(ss)


check_palindrome(ss,nn)
