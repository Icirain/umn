def mergeSort(alist,left,right):
    if (right-left)==1:
        if alist[left]>alist[right]:
            alist[left],alist[right]=alist[right],alist[left]
    elif(right!=left):
        middle=(left+right)//2
        mergeSort(alist,left,middle-1)
        mergeSort(alist,middle,right)
        i=left
        j=middle
        k=left
        temp=list(range(len(alist)))
        while (i<=middle-1)and(j<=right):
            if(alist[i]<=alist[j]):
                temp[k]=alist[i]
                i=i+1
            else:
                temp[k]=alist[j]
                j=j+1
            k=k+1
        if j>right:
            for index in range(middle-i):
                alist[right-index]=alist[middle-1-index]
        for index in range(left, k):
            alist[index]=temp[index]
        print(alist)
alist=[20,18,16,14,12,10,8,6,4,2]
mergeSort(alist,0,len(alist)-1)
print(alist)


     
