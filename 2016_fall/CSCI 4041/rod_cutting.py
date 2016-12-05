class rod_cutting_execution(object):
    def __init__(self,p):
        self.p = p
        self.length = len(self.p)-1
        self.r = list()
        self.s = list()
        for i in range(self.length+1):
            self.r.append(-1)
            self.s.append(0)
        self.r[0] = 0
    def bottom_up(self):
        for i in range(1,self.length+1):
            for j in range(1,i+1):
                if self.r[i] < self.p[j] + self.r[i-j]:
                    self.r[i] = self.p[j] + self.r[i-j]
                    self.s[i] = j
        print self.r
        print self.p
    def memorized_cutting(self,n):
        if self.r[n] >= 0:
            return self.r[n]
        for j in range(1,n+1):
            if self.r[n] < self.p[j] + self.memorized_cutting(n-j):
                self.r[n] = self.memorized_cutting(n-j)
            return r[n]




p = [0,1,5,8,9,10,17,17,20,24,30]
test = rod_cutting_execution(p)
test.bottom_up()
print test.memorized_cutting(5)
