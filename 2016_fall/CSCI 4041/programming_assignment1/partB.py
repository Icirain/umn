class Huffman(object):
    data=[]
    NodeList=[]
    stat={}
    def __init__(self,filename):
        self.filename=filename
        self.read_file()
    def read_file(self):
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
        print(stat)
        self.stat=stat
        for i ,j in stat.iteritems():
            self.data.append([i,j])
    def make_node(self):
        for i in range(len(self.data)):
            new_node=HuffmanNode(self.data[i][0],self.data[i][1])
            self.NodeList.append(new_node)
        self.insertionSort()
    def create_tree(self):
        self.make_node()
        while(len(self.NodeList)!=1):
            temp1=self.NodeList.pop(0)
            temp2=self.NodeList.pop(0)
            if temp1.item not in self.stat:
                temp1.item='0'
            if temp2.item not in self.stat:
                temp2.item='1'
            new_node=HuffmanNode('0',temp1.weight+temp2.weight,temp1,temp2)
            self.NodeList.append(new_node)
            self.insertionSort()
    def search_key(self,item,str,node):
        if node!=None:
            if node.item==item:
                print(str)
            else:
                self.search_key(item,str+'0',node.left)
                self.search_key(item,str+'1',node.right)
    def insertionSort(self):
        for i in range(1,len(self.NodeList)):
            key=self.NodeList[i]
            j=i-1
            while j>=0 and self.NodeList[j].weight>key.weight:
                self.NodeList[j+1]=self.NodeList[j]
                j=j-1
            self.NodeList[j+1]=key




class HuffmanNode(object):
    def __init__(self,item,weight,left=None,right=None):
        self.item=item
        self.weight=weight
        self.left=left
        self.right=right
Huffmancode=Huffman('char_info.txt')
Huffmancode.create_tree()
Huffmancode.search_key('f','',Huffmancode.NodeList[0])
