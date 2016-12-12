import copy
class biconn_execution(object):
    martrix = list()
    #vertices = list()
    #edges = list()
    stack = list()
    parent = list()
    low = list()
    visted = list()
    d = list()
    count = 0
    bridge = list()
    AP = list()
    def __init__(self,filename):
        self.filename = filename
    def read_file(self):
        file = open(self.filename)
        row = file.readline().split()[-1]
        col = file.readline().split()[-1]
        data = list(file)
        if '\n' in data:   #the space of the input stream have not been solved
            data.remove('\n')
        for x in range(len(data)):
            temp = data[x].split()
            for y in range(len(temp)):
                temp[y] = int(temp[y])
            self.martrix.append(temp)
        for i in range(len(self.martrix)):
            print self.martrix[i]
    def Biconn_Compo(self):
        for i in range (len(self.martrix)):
            self.parent.append(None)
            self.visted.append(False)
            self.low.append(-1)
            self.d.append(-1)
        for i in range(len(self.martrix)):
            if self.visted[i] == False:
                self.DFS_Visit(i)
    def DFS_Visit(self,u):
        temp_edges = self.martrix[u]
        child = 0
        isAP = False
        self.visted[u] = True
        self.count += 1
        self.d[u] = self.count
        self.low[u] = self.d[u]
        for i in range (len(temp_edges)):
            if temp_edges[i] == 1:
                if self.visted[i] == False:
                    self.stack.append([u,i])
                    self.parent[i] = u
                    self.DFS_Visit(i)
                    child += 1
                    if self.low[i] >= self.d[u]:
                        self.OutputComp(u,i)
                        isAP = True
                    self.low[u] = min(self.low[u],self.low[i])
                elif self.parent[u] != i and self.d[i]<self.d[u]:
                    self.stack.append([u,i])
                    self.low[u] = min(self.low[u],self.d[i])
        if self.parent[u] == None and child >= 2:
            self.AP.append(u)
        if self.parent[u] != None and isAP:
            self.AP.append(u)
        #print 'vertex:',u
        #print 'low:',self.low[u]
        #print 'd:',self.d[u]
        #print 'parent:',self.parent[u]
    def OutputComp(self,u,v):
        edge = [u,v]
        count = 0
        print 'New Biconn Found'
        while self.stack[-1] != edge:
            count += 1
            print self.stack.pop()
        count += 1
        print self.stack.pop()
        if count == 1:
            self.bridge.append([u,v])
    def present(self):
        print self.bridge
        print self.AP










    # def Extract_Min(self, current_queue):
    #     current_queue.sort(key = lambda vertice:vertice.key)
    #     return current_queue.pop(0)

    # def print_MST(self):
    #     MST = copy.deepcopy(self.martrix)
    #     print MST
    #
    #     for i in range(len(MST)):
    #         for j in range(len(MST[i])):
    #             MST[i][j] = 0
    #     for i in range(len(self.vertices)):
    #         temp = self.vertices[i]
    #         if temp.pi != None:
    #             MST[temp.index][temp.pi] = temp.key
    #             MST[temp.pi][temp.index] = temp.key
    #     for i in range(len(MST)):
    #         print MST[i]


class vertice(object):
    def __init__(self,index,parent):
        self.index = index
        self.parent = parent
class edge(object):
    def __init__(self,node_1,node_2,weight):
        self.node_1 = node_1
        self.node_2 = node_2
        self.weight = weight
test = biconn_execution('graph_e.txt')
test.read_file()
test.Biconn_Compo()
test.present()
