x=str(input("Enter your string"))
def palindrome(x):
    return x== x[::-1]
result=palindrome(x)
if result:
    print("This is palindrome")
else:
    print("This is not palindrome")

