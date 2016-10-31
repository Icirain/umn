def quicksort(alist, left, right):
    if left < right:
        middle=partition(alist, left, right)
        quicksort(alist, left,middle-1)
        quicksort(alist, middle+1, right)
    return alist

def partition(alist, left, right):
    pivot = alist[left]
    l = left+1
    r = right
    i=1
    while (i):
        while l <= r and alist[l] <= pivot:
            l = l + 1
        while alist[r] >= pivot and r >=l:
            r = r -1
        if r < l:
            i=0
        else:
            a[l],a[r]=a[r],a[l]
    alist[left],alist[r]=alist[r],alist[left]
    middle=r
    print(alist)
    return middle

alist=[20,18,16,14,12,10,8,6,4,2]
print(alist)
quicksort(alist,0,len(alist)-1)
print(alist)

