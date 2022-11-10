#Python program to write a list to a file

list=["HTML","CSS","JS","Mysql","Django","React"]
with open("c.txt","w") as f:
    for item in list:
        f.write("%s\n"%item)
print("List has been added")        
f = open("c.txt", "r")
print(f.read())
