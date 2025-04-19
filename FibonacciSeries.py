# Fibonacci Series up to N Terms
# Write a program that prints the Fibonacci sequence up to the N-th term using a loop.
num=int(input("Enter number till you want to print fibonacci"))
def fibonacci(num):
    for i in range(1,num):
        sum=(i-1)+(i-2)
        print(sum)
fibonacci(num)


    
