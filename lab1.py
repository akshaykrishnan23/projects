from datetime import datetime
username=input("Enter your name: ")
age=int(input("Enter your age: "))
hundred = int((100-age) + datetime.now().year)
print ("Hello %s. You are %s years old. You will turn 100 years old in %s." % (username, age, hundred))