import copy
class Prim_execution(object):
    martrix = list()
    vertices = list()
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
    def make_vertices(self):
        for i in range(len(self.martrix)):
            new_vertice = vertice(i,self.martrix[i])
            self.vertices.append(new_vertice)
    def Extract_Min(self, current_queue):
        current_queue.sort(key = lambda vertice:vertice.key)
        return current_queue.pop(0)
    def Prim(self):
        current_queue = list(self.vertices)
        root = current_queue[2]
        root.key = 0
        while len(current_queue) != 0:
            u = self.Extract_Min(current_queue)
            for i in range(len(u.edge)):
                weight = u.edge[i]
                target = self.vertices[i]
                if weight != 0 and target in current_queue and weight<target.key:
                    target.key = weight
                    target.pi = u.index
    def print_MST(self):
        MST = copy.deepcopy(self.martrix)
        print MST
        for i in range(len(MST)):
            for j in range(len(MST[i])):
                MST[i][j] = 0
        for i in range(len(self.vertices)):
            temp = self.vertices[i]
            if temp.pi != None:
                MST[temp.index][temp.pi] = temp.key
                MST[temp.pi][temp.index] = temp.key
        for i in range(len(MST)):
            print MST[i]


class vertice(object):
    def __init__(self,index,edge,key = 20000,pi = None):
        self.index = index
        self.edge = edge
        self.key = key
        self.pi = pi


test = Prim_execution('graph_file.txt')
test.read_file()
test.make_vertices()
test.Prim()
test.print_MST()
