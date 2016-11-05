def read_file(filename):
    file=open(filename)
    content=list(file)
    return content
content=read_file('customers_info.txt')
for x in content[::2]:
    print(x.lstrip(':'))
