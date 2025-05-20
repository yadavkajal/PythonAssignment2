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
