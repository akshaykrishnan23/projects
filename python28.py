#Python program to read a file line by line and store it into a list

with open("c.txt") as f:
    content=f.readlines()
print(content)
    
content= [x.strip() for x in content]
print(content)