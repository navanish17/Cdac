#Qn.1

k  = open("C:\Cdac\Python\excercise_4.py","r")
print(k.read())
k.close()

#Qn.2
file_path = r"C:\Cdac\Python\excercise_5.py"

def countlines(file_path):
    k = open(file_path,'r')
    m = k.readlines()
    k.close()

    lines = len(m)
    print(lines)

def countchar(file_path):
    c = open(file_path,'r')
    d = len(c.read())
    char = d
    c.close()
    count_char = print(char)

def count_both(file_path):
    count_lines = countlines(file_path)
    count_char = countchar(file_path)
    return count_lines, count_char


#import function
import mymod
file_path = input("enter file")
result1 = mymod.countchar(file_path)
result2 = mymod.countlines(file_path)
result3 = mymod.count_both(file_path)


#Qn.3
#mymod.py functions
def countlines(file_path):
    k = open(file_path,'r')
    m = k.readlines()
    k.close()

    lines = len(m)
    print(lines)

def countchar(file_path):
    c = open(file_path,'r')
    d = len(c.read())
    char = d
    c.close()
    count_char = print(char)

def count_both(file_path):
    count_lines = countlines(file_path)
    count_char = countchar(file_path)
    return count_lines, count_char

#importing by all mmethod
#first method
import mymod
file_path = input("enter file")
result1 = mymod.countchar(file_path)

#from second method
from mymod import countlines
result2 = mymod.countlines(file_path)

#from method 3
from mymod import *
result3 = count_both(file_path)

#Qn.4
def countlines(file_path):
    k = open(file_path,'r')
    m = k.readlines()
    k.close()

    lines = len(m)
    print(lines)
    


def countchar(file_path):
    c = open(file_path,'r')
    d = len(c.read())
    char = d
    c.close()
    count_char = print(char)


def count_both(file_path):
    count_lines = countlines(file_path)
    count_char = countchar(file_path)
    return count_lines, count_char

if __name__ == "__main__":
    file_path = input("enter file")
    count_both(file_path)


#Qn.5
import mymodule
file_path = input("enter file")
mymodule.count_both(file_path)

import mymodule
from mymodule import countchar
file_path = input("enter file")
mymodule.countchar(file_path)


#Qn.6
import mypkg.mymod
file_path = input("enter file")
mypkg.mymod.count_both(file_path)

#Qn.7
with open("name.txt") as f:
    k = f.readlines()
n = int(input("desired number of lines"))
for i in range(len(k)):
    if i < n: 
        print(k[i])

#Qn.8
with open("name.txt", 'a') as f:
    f.write("\nI am adding new line here")

k = open("name.txt")
print(k.read())

#Qn.9
with open("name.txt") as f:
    k = f.readlines()
print(k)

#Qn.10
with open("name.txt") as f:
    k = f.readlines()
print(k[::-1])

#Qn.11
n = ['my', 'name', 'is', 'Navanish']
s = str(n)
with open("name.txt",'w') as f:
    f.write(s)

p = open("name.txt")
q = p.read()
print(q)


#Qn.12
def number_lines(file_path):
    k = open(file_path,'r')
    m = k.readlines()
    k.close()

    lines = len(m)
    print(lines)

def number_char(file_path):
    c = open(file_path,'r')
    d = len(c.read())
    char = d
    c.close()
    count_char = print(char)

def number_words(file_path):
    c = open(file_path)
    d = c.read()
    words = len(d.split())
    c.close()
    count_words = print(words)

number_words("name.txt")

#Qn.13
def txt_file():
    while True:
        text = input("enter your text here")
        if text !="END":  
            with open("name.txt",'a') as f:
                f.write(text + "\n")
        else:
            break
    
    with open("name.txt") as f:
        k = f.read()
        q = k.split()
    found = False
    for i in q:
        if i[0].isupper():
            print(i)
            found = True
    if not found:
            print("No uppercase letter found")
txt_file()

#Qn.14
