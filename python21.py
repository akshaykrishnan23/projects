#Python program to generate all sublists of a list

def sublist(a):
   x = [[ ]]
   for i in range(len(a) + 1):    
      for j in range(i + 1, len(a) + 1):         
         sub = a[i:j] 
         x.append(sub) 
   return x
a=list()
n=int(input("Enter the size of the list: "))
print("Enter the Elements of the list: ")
for i in range(int(n)):
   b=int(input(""))
   a.append(b)
print("Sublist is: ",sublist(a)) 