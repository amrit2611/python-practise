# # int = 10
# # string = str(int)
# # print(int, string)

# # print(type(int), type(string))

# # taking input
# # get_name = input("What is you name?\n")

# # print("Your name is " + get_name)

# # strings
# string_data = "hello guys, i am amrit @2611 &^^ 'anything' \"double quotes\""
# print(string_data)
# print(len(string_data))

# # numbers and strings
# x = 5
# y = "5"
# print(str(x) + y) # 55
# print(5 + 5) # 10

# #string detection
# x = "96934hfhldkf"
# y = "69575"

# print(x.isnumeric())
# print(y.isnumeric())

# use_triple = """multi
# line    
# script """
# print(use_triple)

# # number
# x = 3
# y = 45.234
# z = 6 - 3.343j

# print(type(x))
# print(type(y))
# print(type(z))

# # importing random module
# import random
# print(random.random())
# print(random.randint(1,6))
# print(random.choice([4,2,7,9,4,3,6,8,5,4]))
# print(random.sample([30,46,234,64,3], 3))


# # arithmetic operations
# print(100+70)
# print(100-70)
# print(100*70)
# print(100/70)
# print(100%70)
# print(100//70)
# print(100**70)

# # comparison operations
# print(3==3)
# print(2==3)
# print(10>11)
# print(20<=30)
# print(30>=202)

# # logical operators ( and, or, not )
# print(5==5 and 10==10)
# print(10==11 and 11==30)
# print(10==11 or 10==10)
# print(not 5==5)
# print(not False)

# # assignment operator
# x = 5 + 10
# print(x)
# x = 10
# x += 10
# print(x)
# a = 5
# a /= 2
# print(a)

# # conditional operator
# name = "python"
# print("False!" if name!="python" else "True!")

# # lists methods and operations
# numbers = [1,2,3,4,5,6,7,8,9,93,10]
# print(numbers)
# print(numbers[5])
# mixed = ["Hi", [5,7,8], 35, False]
# print(mixed)
# print(len(numbers))
# print(numbers[3:9]) # index 9 not included
# print(numbers[len(numbers) - 2])



# # more operations on lists
# cars = ["bmw", "volvo", "audi"]
# cars[2] = "mercedes" # modifying list
# print(cars)
# cars.append("bugati") # appending to list
# print(cars)
# del cars[2] # deleting from list
# print(cars)

# # tuple
# players = ("dhoni", "sachin", "virat", "sehwag")
# print(players)
# players2 = "messi", "ronaldo", "iniesta", "torres"
# print(players2)
# fruit1 = ("lemon")
# fruit2 = ("orange", )
# print(fruit1)
# print(fruit2)

# list inside tuple
mixed = ("Fruit", 32, [10,20,30,40])
print(mixed)
print(mixed[2])
print(mixed[1:3])

# update tuple
fruits = ("apple", "orange", "lemon", "berry")
print(fruits)
fruits = ("figs", "banana")
print(fruits)

# tuple concatination
print(fruits+mixed)

# del tuple
del fruits
print(fruits)