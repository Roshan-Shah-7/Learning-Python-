# String
# name = "Roshan"

# nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)


# print(nameshort)
# character1 = name[2]
# print(character1)


# same
# print(name[-4:-1])
# print(name[2:5])

# skip value
# print(name[0: 6: 2])
# skiping the value with 1
# OR
# jumping the value with 1 character 

# Length
# print(len(name))

# ends with to check if the value end with.
# print(name.endswith('r'))

# starts with
# print(name.startswith('R'))


# to capitalize
# print(name.capitalize())
# only capitalize the first character

#######################################################

# exercise
# 1: to enter user name and print Good afternoon user_name
# name = input("Enter your name: ")
# print(f"Good Afternoon {name}")

# 2: To fill in a letter
# name = input("Enter your name: ")
# date = '09/5/2024'
# letter = f'''
# Dear {name},
# Your are selected!
# {date}
# '''

# print(letter)

# Another way

# letter = '''
# Dear <|Name|>,
# Your are selected!
# <|Date|>
# '''

# print(letter.replace("<|Name|>", "Roshan").replace("<|Date|>","24 September 2050"))


# 3: program to find double space in a string
# name = "Roshan  Shah"
# print(name.find("  "))


# 4: program to replace double space with single space
# name = "Roshan  Shah"
# print(name.replace("  ", " "))

#5: program to formate the following letter using escape sequence characters
# letter = "Dear Roshan,\nThis python course is nice.\nThank!"
# print(letter)