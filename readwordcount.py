# 8.   Read a File and Count Words
# Write a program that reads a text file and prints the number of words in it

with open ("sample.txt","r") as f:
    data=f.read()
word=data.split()
print(len(word))