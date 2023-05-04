# int = 10
# string = str(int)
# print(int, string)

# print(type(int), type(string))

# taking input
# get_name = input("What is you name?\n")

# print("Your name is " + get_name)

# strings
string_data = "hello guys, i am amrit @2611 &^^ 'anything' \"double quotes\""
print(string_data)
print(len(string_data))

# numbers and strings
x = 5
y = "5"
print(str(x) + y) # 55
print(5 + 5) # 10

#string detection
x = "96934hfhldkf"
y = "69575"

print(x.isnumeric())
print(y.isnumeric())

use_triple = """multi
line    
script """
print(use_triple)

# number
x = 3
y = 45.234
z = 6 - 3.343j

print(type(x))
print(type(y))
print(type(z))

# importing random module
import random
print(random.random())
print(random.randint(1,6))
print(random.choice([4,2,7,9,4,3,6,8,5,4]))
