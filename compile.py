str="read it"
str2=""
print(len(str))
length=len(str)-1
while length>=0:
    str2+=str[length]
    length-=1
print(str2)