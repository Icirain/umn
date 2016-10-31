def insertionSort(alist):
    for index in range(1,len(alist)):
        key=alist[index]
        i=index-1
        while i>=0 and alist[i]>key:
            alist[i+1]=alist[i]
            i=i-1
        alist[i+1]=key
def bucketSort(alist):
  b1=[]
  b2=[]
  b3=[]
  b4=[]
  bucket=[b1,b2,b3,b4]
  for index in range(len(alist)):
      bucket[alist[index]//6].append(alist[index])
  for index in range(len(bucket)):
    print(bucket[index])
  print()
  for index in range(len(bucket)):
      insertionSort(bucket[index])
  for index in range(len(bucket)):
      print(bucket[index])   
  m=0
  for index in range(len(bucket)):
    for i in range(len(bucket[index])):
      alist[m]=bucket[index][i]
      m=m+1
alist=[20,18,16,14,12,10,8,6,4,2]
bucketSort(alist)
print(alist)