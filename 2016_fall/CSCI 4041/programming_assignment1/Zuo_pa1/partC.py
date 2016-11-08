class kmp(object):
    W = ''
    pattern = ''
    def __init__(self, filename):
        self.filename=filename
        self.read_file()
    def read_file(self):    #read the input file and construct pattern string and matching string
        file =  open(self.filename)
        self.W ='!'+file.readline().rstrip('\n')
        self.pattern ='!'+ file.readline().rstrip('\n')
    def make_next(self,pattern):    #function to make the next table
        next=list()
        next.append('!')
        next.append(0)
        k=0
        for i in range(2,len(pattern)):
            while k>0 and pattern[k+1]!=pattern[i]:
                k=next[k]
            if pattern[k+1] == pattern[i]:
                k+=1
            next.append(k)
        return next
    def kmp_matching(self):  # function which implements the kmp matching process
        next=self.make_next(self.pattern)
        k=0
        length=len(self.pattern)-1
        for i in range(1,len(self.W)):
            while k>0 and self.W[i]!=self.pattern[k+1]:
                k=next[k]
            if self.pattern[k+1]==self.W[i]:
                k=k+1
            if k==length:
                position=i-length+1
                print 'START = '+str(position)
                return
test=kmp('string_info.txt')
test.kmp_matching()
