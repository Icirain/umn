class banker(object):
    queue=list()
    def __init__(self,customers_info):
        self.customers_info=customers_info
        self.read_file()
    def read_file(self):
        file=open(self.customers_info)
        content=list(file)
        file.close()
        i=0
        queue=list()
        print(len(content))
        while i<len(content):
            queue.append([content[i].split(':')[1].strip('\n'),int(content[i+1].split(':')[1].strip('\n'))])
            i=i+2
        self.queue=queue
        self.make_heap(len(self.queue))
    def make_heap(self,size):
        for index in range((size-2)//2,-1,-1):
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
        print('List of Customers According to their Priority:')
        while self.queue!=[]:
            self.Extract_Max()
        self.queue=queue
    def Maximum(self):
        print(self.queue[0][0])
    def Extract_Max(self):
        print(self.queue[0][0])
        self.queue.pop(0)
        self.make_heap(len(self.queue))
    def Insert(self,element):
        self.queue.append(element)
        self.make_heap(len(self.queue))
banker1=banker('customers_info.txt')
banker1.print_list()
