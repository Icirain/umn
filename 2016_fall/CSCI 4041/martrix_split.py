class martix_split(object):
    def __init__(self,p):
        self.p = p
        self.length = len(p) - 1
        self.r = list()
        for i in range(len(self.p)):
            temp = list()
            for j in range(len(self.p)):
                temp.append(10000)
            self.r.append(temp)
        for i in range(len(self.p)):
            self.r[i][i] = 0
        print self.length
    def bottom_up(self):
        for l in range(2,self.length+1):
            for i in range(1,self.length-l+2):
                j = i+l-1
            for k in range(i,j):
                temp = self.m[i][k] + self.m[k][j] + self.p[i-1]*self.p[k]*self.p[j]
                if m[i][j] > temp:
                    m[i][j] = temp 








p = [30,35,15,5,10,20,25]
test = martix_split(p)
