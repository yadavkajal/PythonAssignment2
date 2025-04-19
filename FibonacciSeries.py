# 1.	Fibonacci Series up to N Terms
# Write a program that prints the Fibonacci sequence up to the N-th term using a loop.
#fibo logic

num=int(input("Enter a number of fibonacci series count"))
list=[0,1,1]

def fibo(num):
    before=1
    current=1
    for i in range(0,num-(len(list))):
        
        sum=before+current
        before=current
        current=sum
        list.append(sum)

fibo(num)
print(list)

#or
num=int(input("Enter a number of fibonacci series count"))
list=[0,1,1]

def fibo2(num):
    before=1
    current=1
    while num-(len(list))>0:
        
        sum=before+current
        before=current
        current=sum
        list.append(sum)

fibo2(num)
print(list)


""" 
before = 1
current =1 
sum=before+current=2
before=current
current=sum

"""