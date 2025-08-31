#Qn.1
s = 0
for i in range(1,21,2):
    s = i+s
print(s)

#Qn.2
s = 0
for i in range(101,200):
    s = i+s
print(s)

#Qn.3
s = 0
for i in range(2,21,2):
    s = s+(i**2)
print(s)

#Qn.4
my_list = [int(i) for i in input("Enter list values").split(",")]

while True:

    c = int(input("enter your choice: 1,2...9"))
    if c==2:
        print(my_list)
        i = int(input("enter your desired position"))
        v = input("enter your desired value")
        my_list.insert(i,v)
        print(my_list)

    elif c ==1:
        print(my_list)
        v = input("enter your desired value")
        my_list.append(v)
        print(my_list)

    elif c==3:
        print(my_list)
        list2 = [int(i) for i in input("Enter list values").split(",")]
        my_list.append(list2)
        print(my_list)


    elif c==4:
        print(my_list)
        i = int(input("enter your desired position"))
        v = input("enter your desired value")
        my_list[i]=v
        print(my_list)

    elif c==5:
        print(my_list)
        i = int(input("enter your desired position for delete"))
        del my_list[i]
        print(my_list)

    elif c==6:
        print(my_list)
        my_list
        v = input("enter your desired value from the my_list")
        my_list.remove(v)
        print(my_list)

    elif c==7:
        print(my_list)
        my_list.sort()
        print(my_list)

    elif c==8:
        print(my_list)
        my_list.sort(reverse = True)
        print(my_list)

    elif c==9:
        print(my_list)
        print(my_list)

    else:
        break

#Qn.5
for i in range(65,91):
    p = chr(i)
    print(f"{i} = {p}")

#Qn.6
for i in range(48,58):
    p = chr(i)
    print(f"{i} = {p}")

#Qn.7
for i in range(97,123):
    p = chr(i)
    print(f"{i} = {p}")

#Qn.8
l1 = [100,200,300,400,500]
l2 = l1[::-1]
l2

#Qn.9
list1 = [1,2,3,4,5,6,7]
list2 = []
for i in list1:
    list2.append(i**2)

print(list2)

#Qn.10
string = input("Enter you string")
a_count = string.count("a")
e_count = string.count("e")
i_count = string.count("i")
o_count = string.count("o")
u_count = string.count("u")

print(a_count)
print(e_count)
print(i_count)
print(o_count)
print(u_count)

#Qn.11
string = input("write")
string = string.replace(" ","")
str2 = sorted(string)
str2 = "".join(str2)
str2

#Qn.12
word = input("give your input")
word = word.replace(" ","")
import string
k = list(string.punctuation)

s = []
for i in word:
    if i not in k:
        s.append(i)
final = "".join(s)
print(final)

#Qn.13
for i in range(1,4):
    for j in range(i,0,-1):
        print(j, end = "")
    print()

#Qn.14
for i in range(1,7):
    for j in range(i):
        print("*", end = "")
    print()

#Qn.15
for i in range(1,7):
    for j in range(i):
        print("*", end = "")
    print()

for i in range(1,7):
    for j in range(i,7):
        print("*", end = "")
    print()

#Qn.16
for i in range(1,11):
        if i <10:
            print(" ",end="")
        print(i,"| ",end = "")
        for j in range(1,11):
            print(i*j, end = "\t")
        print()

        



