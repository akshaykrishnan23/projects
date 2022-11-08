#Python program to reverse a tuple


def Reverse(tuple):
    new_tuple = tuple[::-1]
    return new_tuple

tuple = ("Honda","Yamaha","Kawasaki","BMW","ducati","aprilla")
print("Tuple          =  ",  tuple)
print("Reversed tuple = " ,  Reverse(tuple))