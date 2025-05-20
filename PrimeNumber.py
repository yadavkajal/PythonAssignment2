# 10.   Find All Prime Numbers in a Range
# Write a program that takes a range (start and end numbers) and returns a list of all prime numbers within that range.

start=int(input("Enter a number from where you start to print prime number"))
end=int(input("Enter a number from where you end to print prime number"))
list=[]
for i in range(start,end+1):
    if(i%1==0 & i%i==0):
        list.append(i)
    
print(list)
