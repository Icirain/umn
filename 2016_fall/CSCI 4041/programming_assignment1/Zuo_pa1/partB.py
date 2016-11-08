class Huffman(object):
    data=[]
    NodeList=[]
    stat={}
    def __init__(self,filename):
        self.filename=filename
        self.read_file()
    def read_file(self):  #function which read the input file and count the frequency of each appeared character
        str=''
        stat={}
        file=open(self.filename)
        for line in file:
            str=str+line.rstrip('\n')
        for i in range(len(str)):
            if str[i] in stat:
                stat[str[i]]+=1
            else:
                stat[str[i]]=1
        #print(stat)
        self.stat=stat
        for i ,j in stat.iteritems():
            self.data.append([i,j])
    def make_node(self):        #function used to construct node for each character. The node instance contains all their information  All the node will be stored into node
        for i in range(len(self.data)):
            new_node=HuffmanNode(self.data[i][0],self.data[i][1])
            self.NodeList.append(new_node)
        self.insertionSort()
    def create_tree(self):   # Towards nodelist. the huffman tree will be constructed by implementing this function
        height=0
        self.make_node()
        while(len(self.NodeList)!=1):
            temp1=self.NodeList.pop(0)
            temp2=self.NodeList.pop(0)
            if temp1.item not in self.stat:
                temp1.item=str(temp1.weight)
            if temp2.item not in self.stat:
                temp2.item=str(temp2.weight)
            new_node=HuffmanNode('0',temp1.weight+temp2.weight,temp1,temp2)
            self.NodeList.append(new_node)
            self.insertionSort()
            height+=1
        self.NodeList[0].item=str(self.NodeList[0].weight)
    def print_tree(self):     #function which is implemented to print out the structure of the huffman tree
        print('Huffman  Tree')
        track_depth=self.NodeList[0].depth
        queue=list()
        queue.append(self.NodeList[0])
        while len(queue)!=0:
            temp=queue.pop(0)
            if temp.depth != track_depth:
                print('\n')
                track_depth=temp.depth
            print '    '+temp.item,
            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)
    '''def level_order(self):
        queue=list()
        queue.append(self.NodeList[0])
        #print('asdjlkj' self.NodeList[0].left.item)
        while len(queue)!=0 :
            temp=queue.pop(0)
            print(temp.item,temp.weight)
            if temp.left!= None:
                queue.append(temp.left)
            if temp.right!=None:
                queue.append(temp.right)   '''
    def depth_deter(self):         #By level_order transversal, the depth of each node of the nodelist will be determined by this function
        queue=list()
        queue.append(self.NodeList[0])
        self.NodeList[0].depth=0
        while len(queue)!=0 :
            temp=queue.pop(0)
            if temp.left!= None:
                self.change_depth(temp.left,temp.depth+1)
                queue.append(temp.left)
            if temp.right!=None:
                self.change_depth(temp.right,temp.depth+1)
                queue.append(temp.right)
    def change_depth(self,node,depth):    #function which is used to change the depth of the node
        node.depth=depth
    def search_key(self,item,str,node):
        if node!=None:
            if node.item==item:
                print node.item+':'+str
            else:
                self.search_key(item,str+'0',node.left)
                self.search_key(item,str+'1',node.right)
    def print_code(self):
        for i in self.stat:
            self.search_key(i,'',self.NodeList[0])
    def insertionSort(self):
        for i in range(1,len(self.NodeList)):
            key=self.NodeList[i]
            j=i-1
            while j>=0 and self.NodeList[j].weight>key.weight:
                self.NodeList[j+1]=self.NodeList[j]
                j=j-1
            self.NodeList[j+1]=key




class HuffmanNode(object):  #HuffmanNode class 
    def __init__(self,item,weight,left=None,right=None,depth=0):
        self.item=item
        self.weight=weight
        self.left=left
        self.right=right
        self.depth=depth
Huffmancode=Huffman('char_info.txt')
Huffmancode.create_tree()
Huffmancode.depth_deter()
Huffmancode.print_code()
Huffmancode.print_tree()

#Huffmancode.search_key('f','',Huffmancode.NodeList[0])
