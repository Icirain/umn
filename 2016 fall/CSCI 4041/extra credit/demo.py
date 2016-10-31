def quickSort(alist,left,right):
    middle=0
    pivot=alist[left]
    l=left
    r=right
    while 1:
        while alist[l]<=pivot:
            if l==r:
                break
            l=l+1
        while alist[r]>pivot:
            r=r-1
        if l<r:
            alist[l],alist[r]=alist[r],alist[l]
        else:
            break
    alist[left],alist[r]=alist[r],alist[left]
    middle=r
    quickSort(alist,left,middle-1)
    quickSort(alist,middle,right)
alist=[20,18,16,14,12,10,8,6,4,2]
quickSort(alist,0,len(alist)-1)
print(alist)