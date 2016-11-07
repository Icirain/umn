class kmp_matching(object):
    W = ''
    pattern = ''
    def __init__(self, filename):
        self.filename=filename
        self.read_file()
    def read_file(self):
        file =  open(self.filename)
        self.W ='!'+file.readline().rstrip('\n')
        self.pattern ='!'+ file.readline().rstrip('\n')
    
test=kmp_matching('string_info.txt')

