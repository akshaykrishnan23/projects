# Python program to remove newline characters from a file
def rmvnwline(fname):
    list = open(fname).readlines()
    return [s.rstrip('\n') for s in list]

print(rmvnwline("c.txt"))


