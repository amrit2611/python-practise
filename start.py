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


# # key value args
# def fruits(fruit1, fruit2, fruit3):
#     print("fruit1: " + fruit1)
#     print("fruit2: " + fruit2)
#     print("fruit3: " + fruit3)
    
    
# fruits("apple", "banana", "orange")


# # passing tuple into function
# def new_func(*fruit):
#     print("the fruit is: " + fruit[2])

# new_func("banana", "apple", "fig")


# # recursion
# def new_recursion(n):
#     if(n>0):
#         result = n + new_recursion(n-1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("\n recursion results")
# new_recursion(20)


# # lambda
# a = lambda x: x * x
# print(a(100))


# # lambda args
# store_lambda = lambda x,y: x*y
# print(store_lambda(20,10000))


# # lambda with function (anonymous arg)
# def new_multiplied(k):
#     return lambda x : x * k

# new_double = new_multiplied(2)
# new_triple = new_multiplied(3)

# print(new_double(12))
# print(new_triple(12))



# ------------------------------   OOPS  ------------------------------------ #

# # classes and objects in python
# class newClass:
#     def newFunc(self):
#         return "python is a lang"
    
# newObj = newClass()

# print(newObj.newFunc())


# # multiple objects on same class
# class newClass:
#     def newHello(self):
#         return "hello! from newHello"
    
# first_object = newClass()              
# print(first_object.newHello())

# second_object = newClass()             
# print(second_object.newHello())

# third_object = newClass()              
# print(third_object.newHello())


# # multiple functions in class
# class doMath:
#     def addition(self, x, y):
#         return x + y
#     def subtraction(self, x, y):
#         if(x<=y):
#             return y-x
#         elif(x>y):
#             return x-y
#     def multiplication(self, x, y):
#         return x*y
    
# my_object = doMath()
# print(my_object.addition(34, 346))
# print(my_object.subtraction(4552, 3463))
# print(my_object.multiplication(3, 547))
    

# # init function  (called automatically whenever class is being used to create an object)
# class newClass:
#     def __init__(self):
#         self.a = "hello"
#         self.b = " world"
        
#     def hi(self):
#         return "hi there"
    
# first_object = newClass()
# print(first_object.a + first_object.b)
# print(first_object.hi())


# # init and object method
# class Player:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def newHi(self):
#         print("Hi, my name is ", self.name, " and my age is ", self.age)
    
# first_player = Player("amrit", 22)
# first_player.newHi()
    
    
# self parameter (representation of the instance of the class)
# self represents the instance of a class
# self is not a keyword in python but is a convention
# not following the convention would lead to our program becoming less readable


# # del keyword
# del first_player.age
# print(first_player/age)   # shows error as the age property no longer exists


# # deleting objects using del keyword
# del first_player
# print(first_player)        # shows error as object first_player no longer exists




# # super class and inheritance
# class Anyone:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
        
#     def display(self):
#         print(self.firstname + " " + self.lastname)
        
# ob1 = Anyone("Amrit", "Dhandharia")
# ob1.display()




# # parent and child class

# # parent class
# class Anyone:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
        
#     def display(self):
#         print(self.firstname + " " + self.lastname)
        
# # child class
# class Player(Anyone):
#     pass                                 # 'pass' used to avoid errors when class definition of child class is empty

# ob1 = Player("Leonel", "Messi")
# ob1.display()




import first_module

first_module.sayHi("Developer")