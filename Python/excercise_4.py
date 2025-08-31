#Qn.1
def calculator():
    x = float(input("enter the value for n1"))
    y = float(input("enter the value of n2"))

    operator = input("enter the operator : +, -, *, /")

    if operator == "+":
        result = x+y

    elif operator == "-":
        result = x-y

    elif operator == "*":
        result = x*y

    else:
        result = x/y  

    print(result)

#Qn.2
num = int(input("enter the terms"))
a,b = 0,1
for i in range(num+1):
    a,b = b,a+b
    print(a)

#Qn.3
terms = int(input("ENTER VALUES"))
b = range(1, terms+1)
k = list(map(lambda x : x**2, b))
k

#Qn.4
list1 = list(map(int,input("ENTER VALUES").split()))

list2 = list(filter(lambda x : x%13==0,list1))

list2

#Qn.5
num = int(input("enter the terms"))
def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)
result = fibo(num)
print(result)


#Qn.6
num = int(input("enter the terms"))
def sum1(num):
    if num==0:
        return num
    else:
        return num + sum1(num-1)
result = sum1(num)
print(result)
        
#Qn.7
s = input("enter the string")
s = s.replace(" ", "")
s = s.lower()

import string
k = string.punctuation
str = []
for i in s:
    if i not in k:
        str.append(i)
       
if str[::]==str[::-1]:  
    print("Given string is palindrome")
else:
    print("given string is not palindrome")

#Qn.8
import string
s = set(string.ascii_lowercase)
pangram = "The quick brown fox jumps over the lazy dog"
k = pangram.lower()
k = k.replace(" ","")
k = set(k)
if k.issubset(s):
    print("this is pangram")
else:
    print("this is not pangram")

#Qn.9
def overlapping():
    list1 = set(input("enter list values").split(","))
    list2 = set(input("enter list values").split(","))
    k = list1.intersection(list2)
    if k == set():
        print("False")
    else:
        print("True")

#Qn.10
def find_longest_word():
    word = input("enter your words").split()
    k = 0
    for i in range(len(word)):
        
        k = max(k, len(word[i]))
        if k == len(word[i]):
            m = word[i]
        
    print("length of longest word is",k, "and longest word is", m)

#Qn.11
def filter_long_words(n):
    word = input("enter your words").split()
    final = []
    for i in word:
        if len(i)>n:
            final.append(i)
    print(final)
