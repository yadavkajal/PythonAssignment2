# 	5.	Count Vowels in a String
# Write a program that counts and displays the number of vowels in a user-provided string.

str=str(input("Enter a string to find no of vowels :"))
def vowels():
    count=0
    for i in str:
        if(i=="a" or i=="e" or i=="i" or i == "o" or i=="u" or i=="A" or i=="I" or i == "E" or i=="O" or i=="U"):
            count+=1
    print(count)
vowels()

#OR


        