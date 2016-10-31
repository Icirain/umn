def selectionSort(alist):
    for i in range(len(alist)):
        min=alist[i]
        minKey=i
        for j in range(i+1,len(alist)):
            if alist[j]<min:
                min=alist[j]
                minKey=j
        temp=alist[i]
        alist[i]=alist[minKey]
        alist[minKey]=temp
        print(alist)
alist=[20,18,16,14,12,10,8,6,4,2]
selectionSort(alist)








