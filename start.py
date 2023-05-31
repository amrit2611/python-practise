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

# # list inside tuple
# mixed = ("Fruit", 32, [10,20,30,40])
# print(mixed)
# print(mixed[2])
# print(mixed[1:3])

# # update tuple
# fruits = ("apple", "orange", "lemon", "berry")
# print(fruits)
# fruits = ("figs", "banana")
# print(fruits)

# # tuple concatination
# print(fruits+mixed)

# # del tuple
# del fruits
# print(fruits)


# # dictionary
# fruit_color = {"banana":"yellow", "apple":"red", "grapes":"green"}
# fruit_color2 = dict({"banana":"yellow", "apple":"red", "grapes":"green"})
# print(fruit_color, fruit_color2)
# print(type(fruit_color), type(fruit_color2))

# # dictionary methods
# print(fruit_color["apple"])
# print(fruit_color.get("banana"))
# print(fruit_color.get("orange")) # none
# # print(fruit_color["strawberry"]) # error
# fruit_color3 = {"banana":["yellow", 43,6,4], "apple":"red", "grapes":"green"}
# print(fruit_color3["banana"][2])

# # dictionary modification
# fruit_color3["apple"] = 35     # modification
# print(fruit_color3)
# fruit_color3["orange"] = "orange"  # addition
# print(fruit_color3)
# del fruit_color3["orange"]      # deletion of an item
# print(fruit_color3)
# del fruit_color3           # deletion of entire dictionary
# print(fruit_color3)


# # sets
# newfruits = {"fig", "lemon", "banana"}
# print(newfruits) # prints random values in no order
# for x in newfruits:
#     print(x)  # prints one by one in no particular order
# print("banana" in newfruits) # value will be boolean
# print("apple" in newfruits) # false
# newfruits.add("orange")  # adds an item
# print(newfruits)

# newfruits.update(["mango", "grapes"])  # to add multiple items
# print(newfruits)

# print(len(newfruits))

# newfruits.remove("fig")  # removes an item from the set
# print(newfruits)

# x = newfruits.pop()  # removes random element from set
# print(x)

# newfruits.clear()  # removes all items from set and makes it an empty set
# print(newfruits)

# del newfruits   # deletes the set completely
# print(newfruits)




# language = ["s", "df", "dfdf", "iyhe", 'iywefdfidfhidf',"dfdfdf","hfuefh8ue"]
# print(language[:-4])  # prints the list with specified number of elements removed 





# # if, else, elif
# num = 25

# if num > 30:
#     print(str(num) + " is greater than 30")
# elif 30 > num > 20:
#     print(str(num) + " is less than 30 and more than 20")
# else:
#     print(str(num) + " is not greater than 30")


# # ternary operator
# print("Smaller than 20" if num < 20 else "Greater than 30")


# # while loop
# x = 2
# while (x < 10):
#     print(x)
#     x = x + 1
#     if(x == 8):
#         break                     # break

# # else in loop
# x = 1
# while (x < 10):
#     print(x)
#     x = x + 1
# else:
#     print("loop is completed")

# # for loop
# num = [5,6,3,7,7,4,2,7,9,4,2,1,35,7,8,9,2]
# for i in num:
#     print(i)
#     if i > 9:
#         break
# else:
#     print("loop completed")
    




# # --------------function-----------------

# def hello_function(name = "amrit"): # give a default value for parameter
#     print("Hello " + name + "!!")
    
# myname = input("Enter your name\n")    
# hello_function(myname)


# # list as parameter 
# def foods(fruit):
#     for x in fruit:
#         print(x)
# my_fruits = ["fig", "apple", "banana"]
# foods(my_fruits)


# # returning value
# def numbers(x):
#     return 10*x
# print(numbers(10))


# key value args
def fruits(fruit1, fruit2, fruit3):
    print("fruit1: " + fruit1)
    print("fruit2: " + fruit2)
    print("fruit3: " + fruit3)
    
    
fruits("apple", "banana", "orange")