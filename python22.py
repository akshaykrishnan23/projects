# Python program to remove an item from a set if it is present in the set

x={1,2,3,4,5,6,7,8,9}
print("Your set is" ,x)
a=int(input("Enter the item to be removed: "))
x.discard(a)
print("Result is: ",x)