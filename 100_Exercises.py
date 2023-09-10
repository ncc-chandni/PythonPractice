### Qudstion 1

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

list_num = []
for num in range(2000, 3201):
    if (num %7 == 0) and (num %5 !=0):
        list_num.append(str(num))
print(','.join(list_num))



### Question 2

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

num = int(input("Please enter the number: \n"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(fact)



### Question 3

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


dict = {}
num = int(input("Please enter the number: \n"))
for i in range(1, num):
    dict[i] = i*i
print(dict)



### Question 4

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

num = input("Please enter the number seperated by space: \n")
lst = num.split(",")
print(tuple(lst))



### Question 5

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()


### Question 6

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# Solution:

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

### Question 7

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

# Solution:
num = input("Enter numbers:")
num = num.split(',')
rownum = int(num[0])
colnum = int(num[1])
multilist = [[0 for col in range(colnum)] for row in range(rownum)]

for row in range(rownum):
    for col in range(colnum):
        multilist[row][col] = row * col

print(multilist)


### Question 8

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# Solution:

lst = input("Enter comma seperated words ")
lst = lst.split(',')
lst.sort()
print(','.join(lst))


### Question 9

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# Solution:

lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)


### Question 10

# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

sentence = input("Please enter")
print(' '.join(sorted(set(list(sentence.split(" "))))))


# ### Question 11

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

num_lst = input("Please enter the numbers: ")
nums = num_lst.split(",")
number_list = [int(x) for x in nums]
final = []
for numb in number_list:
    if numb >= 1000:
        if numb % 5 == 0:
            final.append(numb)

print(final)

### Question 12

# Write a program, which will find all such numbers between 1000 and 3000 
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(len(",".join(values)))

### Question 13

# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
LETTERS = 0
DIGITS = 0
sentence = input("Please enter: ")
for item in sentence:
    if item.isdigit():
        DIGITS += 1
    elif item.isalpha():
        LETTERS += 1

print(DIGITS)
print(LETTERS)
print(sentence)

### Question 14

# Write a program that accepts a sentence and 
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

upper_count = 0
lower_count = 0
sentence = input("Please enter : ")
for item in sentence:
    if item.isupper():
        upper_count += 1
    elif item.islower():
        lower_count += 1

print(f"LOWER CASE {lower_count}")
print(f"UPPER CASE {upper_count}")

### Question 15

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

num = int(input("Please enter a number: "))
total = num*1 + num*11 + num*111 + num*1111
print(total)

### Question 16

# Use a list comprehension to square each odd number in a list. 
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

lst = input("Please enter comma seperated numbers: ")
final = [x for x in lst.split(",") if int(x)%2 != 0]
print(','.join(final))

### Question 17

# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
balance = 0
while True:
    user = input()
    if not user:
        break
    values = user.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        balance += amount
    elif operation == "W":
        balance -= amount
    
print(balance)

### Question 18

# A website requires the users to input username and password to register. 
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords 
# and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
import re
value = []
password_list=[x for x in input().split(',')]
for item in password_list:
    if len(item)<6 or len(item)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",item):
        continue
    elif not re.search("[0-9]",item):
        continue
    elif not re.search("[A-Z]",item):
        continue
    elif not re.search("[$#@]",item):
        continue
    elif re.search("\s",item):
        continue
    else:
        pass
    value.append(item)
print(",".join(value))

### Question 19

# You are required to write a program to sort the (name, age, height) tuples 
# by ascending order where name is string, age and height are numbers. 
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

from operator import itemgetter
lst = []
while True:
    user = input()
    if not user:
        break
    lst.append(tuple(user.split(",")))
print(sorted(lst, key = itemgetter(0,1,2)))

### Question 20
# Define a class with a generator which can iterate the numbers,
#  which are divisible by 7, between a given range 0 and n.

def seven_div(n):
    for i in range(0,n):
        if i % 7 == 0:
            print(i)

seven_div(14)

### Question 21
# Level 3

# Question
# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. 
# Please write a program to compute the distance from current position 
# after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    lst = s.split(" ")
    direction = lst[0]
    steps = int(lst[1])
    if direction == "UP":
        pos[1] += steps
    elif direction =="DOWN":
        pos[1] -= steps
    elif direction =="LEFT":
        pos[0]-= steps
    elif direction =="RIGHT":
        pos[0]+= steps

print(int(math.sqrt((pos[0]**2)+(pos[1]**2))))


### Question 22

# Write a program to compute the frequency of the words from the input. 
# The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1


user = input("Please enter")
lst = user.split(" ")
dict = {}
values = 0
for keys in lst:
    values = lst.count(keys)
    dict[keys] = values


for key,value in dict.items():
    print(f"{key}: {value}")



### Question 23

# Write a method which can calculate square value of number

def square(num):
    return num*num

print(square(5))


### Question 24

# Python has many built-in functions, and if you do not know how to use it, 
# you can read document online or find some books. 
# But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents,
#  such as abs(), int(), raw_input()
# And add document for your own function
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


### Question 25
# Define a class, which have a class parameter and have a same instance parameter.

class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print(f" name is {Person.name} {jeffrey.name}")

### Question 26:
# Define a function which can compute the sum of two numbers.

def add(n1,n2):
    return n1+n2

print(add(1,2))

### Question 27
# Define a function that can convert a integer into a string and print it in console.
def conversion(a):
    return str(a)

print(conversion(1))

### Question 28
# Define a function that can convert a integer into a string and print it in console.
def conversion(a):
    return str(a)

### Question 29
# Define a function that can receive two integral numbers in string form 
# and compute their sum and then print it in console.
def add(n1,n2):
    return n1+n2

print(add(1,2))

### Question 30
# Define a function that can accept two strings as input and 
# concatenate them and then print it in console.
def conct(s1,s2):
    return s1+s2

print(conct("1","2"))

### Question 31
# Define a function that can accept two strings as input and 
# print the string with maximum length in console. 
# If two strings have the same length, 
# then the function should print all strings line by line.
def strngs(s1,s2):
    if len(s1) > len(s2):
        return s1
    elif len(s2) > len(s1):
        return s2
    elif len(s1) == len(s2):
        return s1 , s2
    
print(strngs("everyone","aaaaaaaa"))


### Question 32
# Define a function that can accept an integer number as input 
# and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    elif num % 2 != 0:
        return "Odd"
    
print(even_odd(2))

### Question 33
# Define a function which can print a dictionary 
# where the keys are numbers between 1 and 3 (both included) 
# and the values are square of keys.

def dictonary(n1,n2):
    dic = {}
    for k in range(n1, n2+1):
        v = k*k
        dic[k] = v
    return dic

print(dictonary(1,3))


### Question 34
# Define a function which can print a dictionary where the keys are numbers 
# between 1 and 20 (both included) and the values are square of keys.
def dictonary(n1,n2):
    dic = {}
    for k in range(n1, n2+1):
        v = k*k
        dic[k] = v
    return dic

print(dictonary(1,20))

### Question 35
# Define a function which can generate a dictionary where the 
# keys are numbers between 1 and 20 (both included) and the values are square of keys. 
# The function should just print the values only.
def dictonary(n1,n2):
    dic = {}
    for k in range(n1, n2+1):
        v = k*k
        dic[k] = v
    return dic.values()

print(dictonary(1,20))

### Question 36
# Define a function which can generate a dictionary where the keys are numbers 
# between 1 and 20 (both included) and the values are square of keys. 
# The function should just print the keys only.
def dictonary(n1,n2):
    dic = {}
    for k in range(n1, n2+1):
        v = k*k
        dic[k] = v
    return dic.keys()

print(dictonary(1,20))

### Question 37
# Define a function which can generate and print a list where 
# the values are square of numbers between 1 and 20 (both included).
def lst(n1,n2):
    l = []
    for n in range(n1, n2+1):
        v = n*n
        l.append(v)
    return l

print(lst(1,20))


### Question 38
# Define a function which can generate a list where the 
# values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the first 5 elements in the list.

def lst(n1,n2):
    l = []
    for n in range(n1, n2+1):
        v = n*n
        l.append(v)
    return l[0:5]

print(lst(1,20))


### Question 39
# Define a function which can generate a list where the 
# values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the last 5 elements in the list.

def lst(n1,n2):
    l = []
    for n in range(n1, n2+1):
        v = n*n
        l.append(v)
    return l[-5:]

print(lst(1,20))


### Question 40
# Define a function which can generate a list where the values are square of numbers 
# between 1 and 20 (both included). Then the function needs to print all values except 
# the first 5 elements in the list.


def lst(n1,n2):
    l = []
    for n in range(n1, n2+1):
        v = n*n
        l.append(v)
    return l[5:]

print(lst(1,20))

### Question 41
# Define a function which can generate and print a tuple where 
# the value are square of numbers between 1 and 20 (both included). 
def lst(n1,n2):
    l = []
    for n in range(n1, n2+1):
        v = n*n
        l.append(v)
    return tuple(l)

print(lst(1,20))


### Question 42
# With a given tuple (1,2,3,4,5,6,7,8,9,10), 
# write a program to print the first half values 
# in one line and the last half values in one line. 

t = (1,2,3,4,5,6,7,8,9,10)
print(f"{t[0:5]} \n{t[5:]}")

### Question 43
# Write a program to generate and print another tuple 
# whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). t1= (1,2,3,4,5,6,7,8,9,10)
t2 = []
for n in t1:
    if n%2 == 0:
        t2.append(n)

print(tuple(t2))

### Question 44
# Write a program which accepts a string as input 
# to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

i = input().lower()
if i == "yes":
    print("Yes")
else:
    print("No")


### Question 45
# Write a program which can filter even numbers 
# in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].


li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter((x for x in li if x%2==0) , li)
print(evenNumbers)

### Question 46
# Write a program which can map() to make a list whose elements 
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map((x for x in li if x%2==0) , li)
print(evenNumbers)

### Question 47
# Write a program which can map() and filter() to make a list 
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)

### Question 48
# Write a program which can filter() to make a list 
# whose elements are even number between 1 and 20 (both included).

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)

### Question 49
# Write a program which can map() to make a list 
# whose elements are square of numbers between 1 and 20 (both included).

squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)

### Question 50
# Define a class named American which has a static method called printNationality.
class American():
    def printNationality():
        return print("America")
america = American
america.printNationality()

### Question 51
# Define a class named American and its subclass NewYorker.
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)

### Question 52
# Define a class named Circle which can be constructed by a radius. 
#The Circle class has a method which can compute the area.

from math import pi
class Circle(object):
    def __init__(self,r):
        self.rad = r
        
    def area(self):
        return round(2 * pi * (self.rad ** 2),2)

circle = Circle(5)
print(circle.area())


### Question 53
# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

class Rectangle(object):
    def __init__(self,len,wid):
        self.length = len
        self.width = wid

    def area(self):
        return self.length * self.width
    
rect = Rectangle(4,5)
print(rect.area())

### Question 54
# Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape 
#where Shape's area is 0 by default.

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0
    
    
class Square(object):
    def __init__(self, l):
        self.length = l

    def area(self):
        return self.length ** 2
    
a1 = Shape()
a2 = Square(2)

print(a1.area())
print(a2.area())


### Question 55
# Please raise a RuntimeError exception.
# raise RuntimeError('something wrong')

### Question 56
# Write a function to compute 5/0 and use try/except to catch the exceptions.
### Question 56
# Write a function to compute 5/0 and use try/except to catch the exceptions.


def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')



### Question 57
# Define a custom exception class which takes a string message as attribute.
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
print(error)

### Question 58
# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address. 
# Both user names and company names are composed of letters only.

emailid = input()
username = emailid.split("@")[0]
print(username.title())

### Question 59
# Assuming that we have some email addresses in the "username@companyname.com" format,
#  please write program to print the company name of a given email address. 
# Both user names and company names are composed of letters only.

emailid = input()
name = emailid.split("@")[0]
domain = emailid.split("@")[1]
company = domain.split(".")[0]
print(company.title())


### Question 60
# Write a program which accepts a sequence of words separated by whitespace
#  as input to print the words composed of digits only.
user = input()
lst = user.split(" ")
op = []
for items in lst:
    if items.isdigit():
        op.append(items)

print(op)


### Question 61
# Print a unicode string "hello world".

unicodeString = u"hello world!"
print(unicodeString)


### Question 62
# # Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
# s = input()
# u = unicode( s ,"utf-8")
# print(u)

# 
# ### Question 63

# Write a special comment to indicate a Python source code file is in unicode.
# -*- coding: utf-8 -*-

#----------------------------------------#

### Question 64

# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

num = int(input())
sum = 0
for i in range(num):
    sum += float(i)/float((i+1))

print(sum)

### Question 65

# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# with a given n input by console (n>0).
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))

### Question 66
# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value of f(n) with a given n input by console.

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2) 
        


num = int(input())
print(f(num))

### Question 67
# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program using list comprehension to print the Fibonacci Sequence 
# in comma separated form with a given n input by console.

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))

### Question 68

# Please write a program using generator to print the even numbers 
# between 0 and n in comma separated form while n is input by console.

def Even(num):
    lst = []
    for i in range(0,num):
        if i%2 == 0:
            lst.append(str(i))
    return ",".join(lst)

num = Even(10)
print(num)

### Question 69
# Please write a program using generator to print the numbers 
# which can be divisible by 5 and 7 between 0 and n 
# in comma separated form while n is input by console.

def div(num):
    for i in range(num):
        if i%5 ==0 and i%7 == 0:
            yield i
        
num = int(input())
values = []
for i in div(num):
    values.append(str(i))

print(",".join(values))


### Question 70
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.
li = [2,4,6,8]
for i in li:
    assert i%2==0

### Question 71
# Please write a program which accepts basic mathematic expression 
#from console and print the evaluation result.

expression = input()
print(eval(expression))


### Question 72
# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.

def searching(n):
    lst = [1,2,3,4,5]
    if n in lst:
        return lst.index(n)
    else:
        return "Not found"
    
print(searching(5))


### Question 73
# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.

def searching(n):
    lst = [1,2,3,4,5]
    if n in lst:
        return lst.index(n)
    else:
        return "Not found"
    
print(searching(5))

### Question 74
# Please generate a random float where the value is between 10 and 100 using Python math module.

import random
print(random.random()*100)


### Question 75
# Please generate a random float where the value is between 5 and 95 using Python math module.
import random
print(random.random()*100-5)

### Question 76
# Please write a program to output a random even number between 0 and 10 
# inclusive using random module and list comprehension.
import random
def random_evn():
    return random.choice([x for x in range(0,11) if x%2==0 ])

print(random_evn())


### Question 77
# Please write a program to output a random number, 
# which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))


### Question 78
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

import random
print(random.sample(range(100), 5))


### Question 79
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random
print(random.sample([x for x in range(100,201) if x%2==0],5))

### Question 80
# Please write a program to randomly generate a list with 5 numbers,
#  which are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random
print(random.sample([x for x in range(1,1001) if x%5==0 and x%7==0],5))


### Question 81
# Please write a program to randomly print a integer number between 7 and 15 inclusive.

import random
print(random.randrange(7,16))

### Question 82
# # Please write a program to compress and decompress 
# # the string "hello world!hello world!hello world!hello world!".

# import zlib
# s = b'hello world!hello world!hello world!hello world!'
# t = zlib.compress(s)
# print(t)
# print(zlib.decompress(t))


### Question 83
# Please write a program to print the running time of execution of "1+1" for 100 times.

# from timeit import Timer
# t = Timer("for i in range(100):1+1")
# print(t.timeit())

### Question 84
# Please write a program to shuffle and print the list [3,6,7,8].
import random
lst = [3,6,7,8]
random.shuffle(lst)
print(lst)

### Question 84
# Please write a program to shuffle and print the list [3,6,7,8].
import random
lst = [3,6,7,8]
random.shuffle(lst)
print(lst)


### Question 86
# Please write a program to generate all sentences 
# where subject is in ["I", "You"] and 
# verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

import random
sub = ["I", "You"]
vrb = ["Play", "Love"]
obj = ["Hockey","Football"]

for item in sub:
    for v in vrb:
        for o in obj:
            print(f"{item} {v} {o} ")


### Question 87
# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

lst = [5,6,77,45,22,12,24]
print([x for x in li if x%2!=0])

### Question 88
# By using list comprehension, please write a program to 
# print the list after removing delete numbers 
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
print([x for x in lst if x%5 != 0 and x%7!=0])

### Question 89
# By using list comprehension, please write a program 
# to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
lst = [lst[i] for i in range(len(lst)) if i%2 != 0]
print(lst)


### Question 90
# By using list comprehension, please write a program 
# generate a 3*5*8 3D array whose each element is 0.

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)


### Question 91
# By using list comprehension, please write a program 
# to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
lst = [lst[i] for i in range(len(lst)) if i not in (0,4,5)]
print(lst)



# ### Question 92
# By using list comprehension, please write a program to print 
# the list after removing the value 24 in [12,24,35,24,88,120,155].
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)


### Question 93
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
# write a program to make a list whose elements are intersection of the above given lists.

l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
lst = []
for i in l1:
    for j in l2:
        if i==j:
            lst.append(i)

print(lst)


### Question 94
# With a given list [12,24,35,24,88,120,155,88,120,155], 
# write a program to print this list after removing all duplicate values with original order reserved.

lst = [12,24,35,24,88,120,155,88,120,155]
l1 = []
for item in lst:
    if  item not in l1:
        l1.append(item)

print(l1)

### Question 95
# Define a class Person and its two child classes: Male and Female. 
# All classes have a method "getGender" which can print "Male" for Male class 
# and "Female" for Female class.



class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())


### Question 96
# Please write a program which count and print the 
# numbers of each character in a string input by console.

strng = input()
print(len(strng.replace(" ","")))


### Question 97
# Please write a program which accepts a string from console and print it in reverse order.

strng = input()
lst = strng[::-1]
print(lst)

### Question 98
# Please write a program which accepts a string from console and 
# print the characters that have even indexes.

strng = input()
lst = [strng[i] for i in range(len(strng)) if i%2 == 0]
print(lst) 


# ### Question 99
# Please write a program which prints all permutations of [1,2,3]
import itertools
print(list(itertools.permutations([1,2,3])))


### Question 100
# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have?
def chicken_rabbit(heads,legs):
    for c in range(heads+1):
        r=heads-c
        if 2*c+4*r==legs:
            return c,r
        
    
heads = 35
legs = 94
c_r = chicken_rabbit(heads,legs)
print(c_r)