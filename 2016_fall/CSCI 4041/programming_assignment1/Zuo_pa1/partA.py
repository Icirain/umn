class banker(object):
    queue=list() #list queue is declared to store the sublist which contains the name and priorty
    def __init__(self,customers_info):
        self.customers_info=customers_info
        self.read_file()
    def read_file(self):  #read_file function read the input and construct the list queue
        file=open(self.customers_info)
        content=list(file)
        file.close()
        i=0
        queue=list()
        while i<len(content):
            queue.append([content[i].split(':')[1].strip('\n'),int(content[i+1].split(':')[1].strip('\n'))])
            i=i+2
        self.queue=queue
        self.make_heap(len(self.queue))
    def make_heap(self,size):
        for index in range((size-2)//2,-1,-1):      #After list queue constructed, this function is called to process the queue into a max heap
            self.Heapify(index,size)
        #print(self.queue)
    def Heapify(self,index,size):
        left=2*index+1
        right=2*index+2
        if left<size and self.queue[left][1]>self.queue[index][1]:
            largest=left
        else:
            largest=index
        if right<size and self.queue[right][1]>self.queue[largest][1]:
            largest=right
        if largest!=index:
            self.queue[largest],self.queue[index]=self.queue[index],self.queue[largest]
            self.Heapify(largest,size)
    def print_list(self):
        queue=self.queue
        print('List of Customers According to their Priority:')      #This function print out the list of name by the order of their Priority
        while self.queue!=[]:
            self.Extract_Max()
        self.queue=queue
    def Maximum(self):       #function Maximum returns the name of customer which has the largest priority
        return self.queue[0][0]
    def Extract_Max(self):   #Extract_Max print retruns the sublist which contains the name of customer and his priority. This element will be removed from list queue
        print(self.queue[0][0])
        temp=self.queue.pop(0)
        self.make_heap(len(self.queue))
        return temp
    def Insert(self,element):    #function Insert will insert the element into the list. And the list will be processed again to maintain the heap 
        self.queue.append(element)
        self.make_heap(len(self.queue))
banker1=banker('customers_info.txt')
banker1.print_list()
