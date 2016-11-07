def kmp_pre(p):
    length=len(p)-1
    a=list()
    a.append(0)
    a.append(0)
    k=0
    for i in range(2,len(p)):
        while k>0 and p[k+1]!=p[i]:
            k=a[k]
        if p[k+1]==p[i]:
            k=k+1
        a.insert(i,k)
    return a
def kmp(T,P):
    m=len(P)-1
    n=len(T)-1
    a=kmp_pre(P)
    k=0
    for i in range(1,len(T)):
        while k>0 and P[k+1]!=T[i]:
            k=a[k]
        if P[k+1]==T[i]:
            k=k+1
        if k==m:
            print(i-m+1)
            print('The String match')
            k=a[m]
T='0aaabccbabccbbbccabbbbccccbabbbaabbcccbabccbaaaaaacccbcccba'
P='0bccba'
kmp(T,P)


