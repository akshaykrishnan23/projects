#Python program to copy the contents of a file to another file


with open('c.txt','r') as firstfile, open('c1.txt','a') as secondfile:
     for line in firstfile:
        secondfile.write(line)