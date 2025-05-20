# 9.   Check for Anagrams
#Write a program that checks whether two given strings are anagrams (i.e., they contain the same characters in a different order).


#using simple logic
str1=str(input("Enter the first Word "))
str2=str(input("Enter the Second Word "))
str3=str1.lower()
str4=str2.lower()
res1=sorted(str3)
res2=sorted(str4)
if res1==res2:
    print("Word "+str1+ " & "+ "Word "+ str2+ " Are anagram")
else:
    print("Word "+str1+ " & "+ "Word "+ str2+ " Are not anagram")

#using fucntion

def Anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    #sorting the character and return
    return sorted(str1)==sorted(str2)

string1=str(input("Enter the first Word "))
string2=str(input("Enter the Second Word "))

if Anagram(string1,string2):
    print("The strings are Anagram")
else:
    print("The string are not Anagram")

    