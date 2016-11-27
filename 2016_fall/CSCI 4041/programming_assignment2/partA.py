class Prim_execution(object):
    martrix = list()
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
    


test = Prim_execution('graph_file.txt')
test.read_file()
