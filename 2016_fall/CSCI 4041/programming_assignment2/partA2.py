import copy
class Kruskal_execution(object):
    martrix = list()
    vertices = list()
    edges = list()
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
                if temp[y] != 0:
                    new_edge = edge(x,y,temp[y])
                    self.edges.append(new_edge)
            self.martrix.append(temp)
    def make_vertices(self):
        for i in range(len(self.martrix)):
            new_vertice = vertice(i,i)
            self.vertices.append(new_vertice)
    def Find(self,x):
        if x.parent != x.index:
            return self.Find(self.vertices[x.parent])
        return x.parent
    def Union(self,x,y):
        xRoot = self.Find(x)
        yRoot = self.Find(y)
        if xRoot == yRoot:
            return
        self.vertices[xRoot].parent = yRoot
    def Kruskal(self):
        MST = list()
        temp_edges = copy.deepcopy(self.edges)
        temp_edges.sort(key = lambda edge:edge.weight)
        for i in range(len(temp_edges)):
            temp = temp_edges[i]
            vertice_1 = self.vertices[temp.node_1]
            vertice_2 = self.vertices[temp.node_2]
            if self.Find(vertice_1) != self.Find(vertice_2):
                print self.Find(vertice_1),self.Find(vertice_2)
                self.Union(vertice_1,vertice_2)
                print vertice_1.index,vertice_2.index
                MST.append(temp)
        return MST







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
test = Kruskal_execution('graph_file.txt')
test.read_file()
test.make_vertices()
MST = test.Kruskal()
print len(MST)
