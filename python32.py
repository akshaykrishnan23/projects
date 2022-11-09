#Python program to count the number of lines in a text file
f="c.txt"
with open(f , "r") as file:
    lines=len(file.readline())
    print("Total number of lines: ",lines)
    