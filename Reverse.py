# Reverse a String
# Write a program that takes a string as input and prints its reverse.

EnterStr=str(input("Enter something which you want to print in reverse order: "))

def rev():
    str=""
    for i in EnterStr:
        str=i +str
    print(str)
rev()

#refer palindrom for more ways
