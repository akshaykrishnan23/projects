#Python program to read a file line by line store it into an array
import array
f=open("c.txt","r")
array=[]
for line in f:
    array.append(line)
array= [x.strip() for x in array]
print(array)

