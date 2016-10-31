def insertionSort(alist):
    for index in range(1,len(alist)):
        key=alist[index]
        i=index-1
        while i>=0 and alist[i]>key:
            alist[i+1]=alist[i]
            i=i-1
        alist[i+1]=key
        print(alist)
alist=[20,18,16,14,12,10,8,6,4,2]
insertionSort(alist)
print(alist)