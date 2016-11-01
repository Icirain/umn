import os
a=input()
print(os.path.isfile(a))
print(bin(os.stat(a).st_mode)[-3])