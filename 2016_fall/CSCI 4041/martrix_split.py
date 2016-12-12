class martix_split(object):
    def __init__(self,p):
        self.p = p
        self.length = len(p) - 1
        self.r = list()
        for i in range(len(self.p)):
            temp = list()
            for j in range(len(self.p)):
                temp.append(10000000)
            self.r.append(temp)
        for i in range(len(self.p)):
            self.r[i][i] = 0
        print self.length
    def bottom_up(self):
        for l in range(2,self.length+1):
            for i in range(1,self.length-l+2):
                j = i+l-1
                for k in range(i,j):
                    print i,j,k
                    temp = self.r[i][k] + self.r[k+1][j] + self.p[i-1]*self.p[k]*self.p[j]
                    print temp
                    if self.r[i][j] > temp:
                        self.r[i][j] = temp
        print self.r








p = [30,35,15,5,10,20,25]
test = martix_split(p)
test.bottom_up()
