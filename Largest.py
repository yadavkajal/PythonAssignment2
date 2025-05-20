# 4.	Find the Largest Element in a List
# Write a program that takes a list of numbers and finds the largest element.
list=[98,76,54,67,89,57,68,99,34]
def largest_num():
    print(max(list))

largest_num()

#or
list=[98,76,54,67,89,57,68,99,34]

def largest():
    largest=list[0]
    for val in list:
        if(val>largest):
            largest=val
    print(largest)
largest()
        
#or
list=[98,76,54,67,89,57,68,99,34]
def largest2():
    list.sort(reverse=True)
    print(list[0])
largest2()