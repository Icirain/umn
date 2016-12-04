import copy
import math
class Floydw_execution(object):
    martrix = list()
    pi_martrix = list()
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
    def present(self):
        for i in range(len(self.martrix)):
            print self.martrix[i]
        for i in range(len(self.pi_martrix)):
            print self.pi_martrix[i]
    def make_pi(self):
        for i in range(len(self.martrix)):
            temp = list()
            for j in range(len(self.martrix[i])):
                if i == j or self.martrix[i][j] == 10000:
                    temp.append('NULL')
                else:
                    temp.append(i)
            self.pi_martrix.append(temp)
    def Floydw(self):
        temp = copy.deepcopy(self.pi_martrix)
        for round in range(len(self.martrix)):
            for i in range(len(self.martrix)):
                for j in range(len(self.martrix[i])):
                    new_road = self.martrix[i][round] + self.martrix[round][j]
                    if new_road < self.martrix[i][j]:
                        self.martrix[i][j] = new_road
                        self.pi_martrix[i][j] = self.pi_martrix[round][j]



class vertice(object):
    def __init__(self,index,parent):
        self.index = index
        self.parent = parent
class edge(object):
    def __init__(self,node_1,node_2,weight):
        self.node_1 = node_1
        self.node_2 = node_2
        self.weight = weight
test = Floydw_execution('partB_file.txt')
test.read_file()
test.make_pi()
test.Floydw()
test.present()
