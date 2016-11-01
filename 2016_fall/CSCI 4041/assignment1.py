def median(a,length):
    if length%2==0:
        return (a[length//2]+a[length//2-1])/2
    else:
        return a[length//2]
def getMedian(a,b,length):
    if length<=0:
        return -1
    elif length==1:
        return (a[0]+b[0])/2
    elif length==2:
        return (max(a[0],b[0])+min(a[1],b[1]))/2
    m1=median(a,length)
    m2=median(b,length)
    print(a)
    print(b)
    print(m1)
    print(m2)
    if(m1==m2):
        return m2
    elif m1<m2:
        if length%2==0:
            return getMedian(a[length//2:],b[:length//2],length//2)
        else:
            return getMedian(a[length//2:],b[:length//2+1],length//2+1)
    elif m1>m2:
        if length%2==0:
            return getMedian(a[:length//2],b[length//2:],length//2)
        else:
            return getMedian(a[:length//2+1],b[length//2:],length//2+1)
a=[5,6,7,20,22]
b=[1,2,11,31,32]
print(getMedian(a,b,len(a)))

