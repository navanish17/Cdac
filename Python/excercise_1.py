#qn.1
import math
r = float(input("Enter the circle radius : "))

const = math.pi
area = const*r**2
print(area)

#qn.2
temp = float(input("enter the temperature in ferenhite : "))

degree = 5/9*(temp-32)

print(degree)

#qn.3
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


#qn.4
number = float(input("give me the number "))

square_root = math.sqrt(number)
print(square_root)

#qn.5
import cmath
a= float(input("enter the value of a "))
b= float(input("enter the value of b "))
c= float(input("enter the value of c "))

base = cmath.sqrt(b**2-4*a*c)

root1 = (-b+base)/2*a

root2 = (-b-base)/2*a

print(root1)
print(root2)


#qn.6
a= float(input("enter the value of a "))
b= float(input("enter the value of b "))
c= float(input("enter the value of c "))

s= (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)

#qn.7
number = int(input("enter the 5 digit number "))

a = number%10

b = (number//10)%10

c = (number//100)%10

d = (number//1000)%10

e = (number//10000)%10

Add = a+b+c+d+e

print(Add)

#qn.8

string = ''' Twinkle, twinkle, little star,\n \t How I wonder what you are!\n\t Up above the world so high,\n Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are'''

print(string)

#qn.9

profile = (" my name is navanish\n my age is 24\n my address is mumbai")

print(profile)

#qn.10
string = "My name is 'Navanish Pandey' and\n\
                my age is '24' "
print(string)

#qn.11
string = """ My name is "Navanish Pandey" and 
                my age is '24' """
print(string)


#qn.12

a=input()
b=ord(a)
print(b)
#use char keyword to askey number to char

#qn.13
string = "abc "*5

print(string)

#qn.14
dashes = '-'*50

print(dashes)

#qn.15

string = "abc"

name = str.upper(string)
name

#qn.16
string = "this is noida"

str1 = string[:2]

str2 = string[-2:]

add = str1+str2
add

#qn.17
string = "restart"
b = list(string)
b[5]= "$"
b = "".join(b)
b

#qn.18
string = ('abc', 'xyz')
a = list(string)
b = list(a[0])
c = list(a[1])
c[2],b[2]=b[2],c[2]
print("".join(c) + " " + "".join(b))

#OR
string1 = "abc"
string2 = "xyz"
print(string2[0:2]+string1[-1]+ " " + string1[0:2]+string2[-1])




