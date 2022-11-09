#Python program to append text to a file and display the text

lines=["Python","This is python test file"]

with open ('c.txt', 'w') as file:  
    for line1 in lines:  
        file.write(line1)  
        file.write("\n")  
with open("c.txt", 'a') as file1:
    file1.write("Python is awesome")
with open("c.txt", "r") as file1:
    print(file1.read())