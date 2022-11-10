 #Python program to get the file size of a plain file
import os
def file_size(file):
    statinfo = os.stat(file)
    return statinfo.st_size

print("File size of a plain file: ",file_size("c.txt"))