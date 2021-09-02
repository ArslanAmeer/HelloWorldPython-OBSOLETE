# ========== BASIC Beginners Practice ==========


# --- Print or Comments
# print('*' * 15)

# --- Variables, input andType Conversion
# birthYear = input('birthYear: ')
# print(type(birthYear))
# age = 2021 - int(birthYear)  #float() str()
# print(type(age))
# print('Your age is: ' + str(age))

# --- Strings
# msg = '''Hi,
# John,
# Hope you are good.
# Bye.'''
#
# print(msg)
# print(msg[0])
# print(msg[-1])
# print(msg[1:-1])


# --- Formatted String
# first = 'Arslan'
# last = 'Ameer'
# msg = f'{first} full name is {first} {last}'
# print(msg)


# --- String Methods
# course = 'Python for beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.lower().find('p'))
# print(course.lower().replace('beginners', 'noobs'))
# print(course.replace('y', 'i'))
# print(course)
#
# print('Python' in course)


# --- Arithmetic Operators
# print(10 / 3)  # divide with floating point
# print(10 // 3)  # divide with integer
# print(10 % 3)  # modulas
# print(10 ** 3)  # 10 ^3
# print(10 + 3 * 2) # Operator Precedence (PEMDAS)

# --- Math Function
# import math
# x = 2.5
# print(round(x))
# print(abs(x))
# print(math.ceil(x))
# print(math.floor(x))

# --- If statement
# isHot = False
# isCold = True
#
# if isHot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif isCold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# --- Logical Operator
# hasHighIncome = True
# hasGoodCredit = False
#
# if hasHighIncome and hasGoodCredit:
#     print("Eligible for loan")
#
# if hasHighIncome or hasGoodCredit:
#     print("Eligible for loan")
#
# if hasHighIncome and not hasGoodCredit:
#     print("Not Eligible for loan")

# --- Comparison operators

# userWeight = int(input("Weight: "))
#
# unit = input("(L)bs or (K)g: ")
#
# if unit.lower() == 'l':
#     print(f'You are {userWeight * 0.45} Kg')
# elif unit.lower() == 'k':
#     print(f'You are {userWeight / 0.45} lbs')
# else:
#     print('Wrong Unit added')

# --- While loops
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
#
# print('end')
#
# guess = False
# i = 1
# while i <= 3:
#     num = int(input('guess Number: '))
#     if num == 9:
#         print('You Guessed it right')
#         break
#     i = i + 1
# else:
#     print('Sorry You have failed')

# Car Game
# isCarRunning = False
# while True:
#     command = input('>')
#     if command.lower() == 'help':
#         print(''' We support:
#         start
#         stop
#         quit
#         commands''')
#     elif command.lower() == 'start':
#         if isCarRunning:
#             print('car is already running')
#         else:
#             print('vroom vroom... start...')
#             isCarRunning = True
#
#     elif command.lower() == 'stop':
#         if isCarRunning:
#             print('car stopped')
#             isCarRunning = False
#
#         else:
#             print('car is already stopped')
#
#     elif command.lower() == 'quit':
#         break
#
#     else:
#         print('Sorry i did not understand')

# --- For loops

# for item in 'Python':
#     print(item)

# for item in ['arslan', 'mujahid']:
#     print(item)

# for item in range(10):  # range(5,10)  range(5,10,2)
#     print(item)

# numbers = [5, 2, 5, 2, 2]
#
# for item in numbers:
#     print('x' * item)

# --- Lists
# numbers = [10, 5, 300, 55, 2]
# maxNumb = numbers[0]
# for num in numbers:
#     if num > maxNumb:
#         maxNumb = num
#
# print(maxNumb)

# --- 2D lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# --- List Methods

# numbers = [1, 2, 3, 3, 4, 4, 1]
#
# numbers.append(20)
# print(numbers)
#
# numbers.insert(0, 5)
# print(numbers)
#
# numbers.remove(3)
# print(numbers)
#
# numbers.pop()
# print(numbers)
#
# print(numbers.index(4))
#
# print(4 in numbers)
#
# print(numbers.count(1))
#
# numbers.sort()
# print(numbers)
#
# numbers.reverse()
# print(numbers)
#
# numbers2 = numbers.copy()
#
# for item in numbers:
#     count = numbers.count(item)
#     if count > 1:
#         numbers.remove(item)
#
# print(numbers)
#
# numbers = [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
#
# print(unique)


# --- Tuples

# numbers = (1, 2, 3, 4)

# --- Unpacking

# coordinates = (1, 2, 3)
# x, y, z = coordinates

# --- Dictionaries

# customer = {
#     "name": "Customer",
#     "age": 36,
#     "isVerified": True,
# }
#
# # print(customer.get('look', 'stylish'))  # .get is able to return default value
# phone = input('Phone: ')
#
# digitsMap = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "Four"
# }
# output = ""
# for dig in phone:
#     output += digitsMap.get(dig, '-') + " "
#
# print(output)


# --- Emoji Converter

# mesg = input(">")
# words = mesg.split(" ")
# emojis = {
#     ":)": "😊",
#     ":(": "😊"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
#
# print(output)

# --- Functions

# def emoji_converter(msg):
#     words = msg.split(" ")
#     emojis = {
#         ":)": "😊",
#         ":(": "😊"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#
#     return output
#
#
# mesg = input(">")
# print(emoji_converter(mesg))


# --- Exceptions
# try:
#     age = int(input("Age: "))
#     nm = 200/age
#     print(age)
# except ValueError:
#     print("Invalid Value")
# except ZeroDivisionError:
#     print('age cannot be zero')

# --- CLASSES

# class Point:
#
#     def __init__(self, x, y):  # this is constructor
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print('move')
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10, 20)
# print(point1.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, i am {self.name}")
#
# per = Person('basheer')
# per.talk()

# --- INHERITENCE

# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     pass
#
#
# class Cat(Mammal):
#     def annoying(self):
#         print('annoying')
#
#
# anm1 = Cat()
# anm1.walk()
# anm1.annoying()

# --- Modules

# import converters
# from converters import lbs_to_kg
#
# print(converters.lbs_to_kg(70))
#
# lbs_to_kg(100)

#import utils
#
# nolists = [3, 6, 2, 4, 8, 14, 7]
#
# # print(utils.find_max(nolists))
#
# print(max(nolists))


# --- PACAKAGES
from ecommerce import shipping

shipping.calc_shipping()