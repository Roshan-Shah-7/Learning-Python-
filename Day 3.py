# List
# List is similar to array
# we can store any data type.
# list are mutable means data can easy change without creating new list

# friends = ['apple', 'Roshan', 7, 7.77, True]

# list are mutable
# we can change the values

# friends[0] = 'banana'

# print(friends)

# print(friends[1:4])

# l1 = [1,3,7,4,5,6,2]

# Methods :
# l1.append(3)
# l1.sort()
# l1.reverse()
# l1.pop(3)
# print(l1)




# Tuples
# tuples are like list but they are un-mutable
# cannont change the value of tuple list

# a = (1,2,3,4,5)
# b = (1,) # to show this is tuple if we don't use comma then python think that it is integer
# print(type(a))

# Exercise
#1: WAP to store seven fruits in a list entered by user.

# fruits = [];
# f1 = input("Enter fruit name: ")
# fruits.append(f1)

# f2= input("Enter fruit name: ")
# fruits.append(f2)

# f3 = input("Enter fruit name: ")
# fruits.append(f3)

# f4 = input("Enter fruit name: ")
# fruits.append(f4)

# f5 = input("Enter fruit name: ")
# fruits.append(f5)

# f6 = input("Enter fruit name: ")
# fruits.append(f6)

# f7 = input("Enter fruit name: ")
# fruits.append(f7)

# print(fruits)

# 2: WAP to accept marks of 6 students and display in sorted manner.

# marks = []

# std1 = int(input("Enter your marks: "))
# marks.append(std1)
# std2 = int(input("Enter your marks: "))
# marks.append(std2)
# std3 = int(input("Enter your marks: "))
# marks.append(std3)
# std4 = int(input("Enter your marks: "))
# marks.append(std4)
# std5 = int(input("Enter your marks: "))
# marks.append(std5)
# std6 = int(input("Enter your marks: "))
# marks.append(std6)

# marks.sort()
# print(marks)

# 3: WAP to sum a list with 4 numbers
# numbers = [1,2,3,4]
# sum = numbers[0] + numbers[1] + numbers[2] + numbers[3]
# print(sum)

# OR
# using sum() function
# print(sum(numbers))


# 4: WAP to count 0's in the following tuple: 

# a = (7,0,8,0,0,9)

# count() funtion which is use to count the repeated number
# n = a.count(0)
# print(n)