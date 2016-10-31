def nextTable(pattern):
    length=len(pattern)
    next=list()
    next.append(-1)
    next.append(-1)
    next.append(0)
    for i in range(3,length):
        j=next[i-1]+1
        while pattern[j]!=pattern[i-1] and j>0:
            j=next[j]+1
        next.append(j)
    return next
def kmp(pattern,a):
    n=len(a)
    m=len(pattern)
    next=nextTable(pattern)
    start=0
    i=1
    j=1
    while i<n and start==0:
        if a[i]==pattern[j]:
            i=i+1
            j=j+1
            print(i,j)
        else:
            j=next[j]+1
            if j==0:
                j=1
                i=i+1
        if j==m:
           start=i-m
    return start
a='0aabababababbaabbaabb'
pattern='0aabb'
print(kmp(pattern,a))

