#Python program to combine each line from first file with the corresponding line in second file

with open('c.txt') as firstfile, open('c1.txt') as secondfile:
    for line1,line2 in zip (firstfile,secondfile):
        print(line1+line2)