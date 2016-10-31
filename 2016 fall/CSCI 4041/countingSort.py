def initCount(a,n,k):
    length=n
    b=list()
    output=list()
    for index in range(0,k):
        b.insert(index,0)            #initial the counting array
    for index in range(0,length):     
        output.insert(index,0)       #initial the output array
    for index in range(0,length):    
        i=a[index]
        b[i]=b[i]+1 
        print(b)                 #count the number of every item in a[0] by counting array
    for index in range(1,len(b)):
        b[index]=b[index-1]+b[index]  #operations in determining the position of item in output[]
        print(b)
    for index in range(length-1,-1,-1):
        i=a[index]
        b[i]=b[i]-1
        output[b[i]]=i                #insert the item in a[] in to output[] with right position to make it sorted
    print(output)
a=[7,1,3,1,2,4,5,7,2,4,3]
initCount(a,len(a),len(a)*2)

