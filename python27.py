#Python program to read last n lines of a file

file="c.txt"
n=int(input("Enter the n value"))
with open(file,"r") as ftest:
    lines=ftest.readlines()
    for textline in (lines[-n:]):
        print(textline, end ='')
ftest.close()