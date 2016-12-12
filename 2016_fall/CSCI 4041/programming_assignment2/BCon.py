class edge:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def BiconnectedComponents(matrix):
    n = len(matrix[0])
    count = 0
    stack = list()
    visited = [0 for x in range(n)]  #0 means False
    parent = [-1 for x in range(n)] #since vertex could be 0, we should use -1 as initialization
    d = [0 for x in range(n)]
    low = [0 for x in range(n)]
    AP = list()   #list for record articulation points
    bridge = list() #list for record bridge
    for i in range(n):
        if visited[i] == 0:
            DFSVisit(i, matrix, count, stack, visited, parent, d, low, AP, bridge)
    Outputbridge(bridge) #print all the bridge
    AP.sort()
    print 'articulation points', AP

def DFSVisit(u, matrix, count, stack, visited, parent, d, low, AP, bridge):
    visited[u] = 1
    count = count + 1
    d[u] = count
    low[u] = count
    isAP = False
    child_count = 0 #count child to determine whether root is an AP
    for v in range(len(matrix[u])):
        if matrix[u][v] == 0:
            continue    #no edge between u,v or self-loop
        elif visited[v] == 0:
            new_edge = edge(u, v)
            stack.append(new_edge)
            parent[v] = u
            child_count = child_count + 1
            DFSVisit(v, matrix, count, stack, visited, parent, d, low, AP, bridge)
            if low[v] >= d[u]:
                isAP = True
                OutputComp(stack, u, v, bridge)
            low[u] = min(low[u], low[v])
        elif parent[u] != v and d[v] < d[u]:
            new_edge = edge(u, v)
            stack.append(new_edge)
            low[u] = min(low[u], d[v])
        #print 'vertex:',u
        #print 'low:',low[u]
        #print 'd:',d[u]
        #print 'parent:',parent[u]
    if parent[u] == -1 and child_count >=2:
        AP.append(u)  ##check if root is an AP
    if parent[u] != -1 and isAP:
        AP.append(u) ##check if other vertex is an AP


def OutputComp(stack, u, v, bridge):
    count = 0
    print "New Biconnected Component Found"
    while not isEmpty(stack):
        count = count + 1
        e = stack.pop()
        print e.x, "--", e.y
        if e.x == u and e.y == v:
            break
    if count == 1:
        #bridge is the BiconnectedComponent which only have two vertex(one edge)
        bridge_edge = edge(u, v)
        bridge.append(bridge_edge)

def isEmpty(stack):
    return stack == []

def Outputbridge(bridge):
    n = len(bridge)
    if n == 0:
        return None
    print 'bridge:'
    for i in range(len(bridge)):
        e = bridge[i]
        print e.x,"--",e.y

#Test cases:
#file = open('graph_c.txt')   ##this is the first example in our discussion
#file = open('graph_d.txt')   ##this is the second example in our discussion
file = open('zhou.txt')   ##this is the example in the material on moodle
rows = file.readline().split()[-1]
cols = file.readline().split()[-1]
rows = int(rows)
cols = int(cols)
matrix = [[0 for x in range(rows)] for y in range(cols)]
data = list(file)
data = data[1:] #The first element is some words
for x in range(len(data)):
    temp = data[x].split()
    for y in range(len(temp)):
        if x == y:
            continue
        temp[y] = int(temp[y])
        if temp[y] != 0:
            matrix[x][y] = 1
#Call the main function
BiconnectedComponents(matrix)
for i in range(len(matrix)):
    print matrix[i]
