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

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print('x' * item)
