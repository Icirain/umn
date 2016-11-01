def HeapiFy(alist,i,heap_size):
    left=2*i
    right=2*i+1
    print(left,right)
    if left<=heap_size and alist[left]>alist[i]:
        largest=left
    else:
        largest=i
    if right<=heap_size and alist[right]>alist[largest]:
        largest=right
    if largest!=i:
        alist[i],alist[largest]=alist[largest],alist[i]
        HeapiFy(alist,largest,heap_size)
def buildHeap(alist):
    length=len(alist)-1
    heap_size=length
    for index in range(length//2,0,-1):
        HeapiFy(alist,index,heap_size)
def HeapSort(alist):
    buildHeap(alist)
    length=len(alist)-1
    heap_size=length
    for index in range(length,1,-1):
        alist[1],alist[index]=alist[index],alist[1]
        heap_size=heap_size-1
        HeapiFy(alist,1,heap_size)
alist=[21,4,1,5,46,2,45,3,65,8,9]
HeapSort(alist)
print(alist)
