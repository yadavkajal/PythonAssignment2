data=str(input("Enter a string: "))
reversed_string = data[::-1]
def reverse():
    if data==reversed_string:
        print("Palindrom")
    else:
        print("Not a Palindrom")
reverse()

#or
palindrom="did it"
reversed_string=""
for char in palindrom:
    reversed_string=char+reversed_string
    
print(reversed_string)

if char==reversed_string:
    print("palindrom")
else:
    print("not a palindrom")

#or
str="New bie"
reverse="".join(reversed(str))
print(reverse)

#or
str="read it"
str2=""
length=len(str)-1
while length>=0:
    str2+=str[length]
    length-=1
print(str2)
