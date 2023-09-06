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
