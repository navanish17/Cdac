#qn.1
list = [1,2,3,4,5]

result  = sum(list)
print(result)

#qn.2
list = [1,2,3,4,5]

result  = max(list)
print(result)

#qn.3
list = [1,2,3,4,5]

result  = min(list)
print(result)

#qn.4
color_list = ['Red', 'Green', 'White', 'Black']

first_colour = color_list[0]
last_color = color_list[-1]

print(first_colour)
print(last_color)

#qn.5
str = input("enter your word")

if str[-3:]=="ing":
    print(str + "ly")

else:
    print(str + "ing") 

#qn.6
score = int(input("Student got the score"))

if score >= 60:
    print("First divison")
elif 59>=score>=50:
    print("Seconnd divison")

elif 49>=score>=40:
    print("third divison")
else:
    print("fail")

#qn.7
num1 = int(input("enter your number1" ))
num2 = int(input("enter your number2" ))
num3 = int(input("enter your number3" ))

list1 = []
list1.extend([num1,num2,num3])

result = max(list1)

print(result)

#qn.8
year = int(input("enter the year"))


if year%400 == 0:
    print("This is leap year")
elif year%100 == 0:
    print("This is not leap year")
elif year%4==0:
    print("this is leap year")


else:
    print("this is not a leap year")

#qn.9
str = input("enter your input")

str1 = list(str)
str1.reverse()
str1 = "".join(str1)

if str1 == str:
    print("This is palindrome")
else:
    print("This is not palindrome")

#qn.10
list1 = ["a", "b",["c",["d", "e",["f","g"],"k"],"l"],"m","n"]

list1[2][1][2].extend(["h","i","j"])

list1

#qn.11
s = [5,10,15,20,25,20]

ind = s.index(20)
s[ind] = 200
s

#qn.12
s= [1,2,3,4,5]
s1 = s[-2:]
s2 = s[0:3]
string = s1+s2
string
