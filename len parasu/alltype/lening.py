# a = "hollo world"
# print (a)

# a = 3
# b = 6  
# print (a + b)
# welcome border
# line1 = "********************"
# line2 = "                    "
# line3 = "welcome to pkreddark"

# print(line1)
# print(line2)
# print(line3)
# print(line2)
# print(line1)
# math
# a = 1
# a += 1
# a =+ 1
# print(a)
#  math
# a = 10.0
# round(a)
# 40 == 40
# 40 != 100
# 40 != 40
# 20 > 10
# 20 < 10
# 20 <= 10
# 20 >= 10
# bool
# x = True
# y + False
# not x
# x and y
# x or y
# if else code
# a = 9
# if a > 4:
#     print ("hi")
# elif a < 4:
#     print("to")
# else:
#     print("welcome")

# singel line code
# a = 1
# print("hi") if a>4 else print("welcome")

# string data type 
# Literal assignment
# First_Name = str(input("Enter the First Name:"))
# last_Name = str(input("Enter the Last Name:"))
# Full_Name = First_Name + last_Name + "!"
# print(Full_Name)

# find data type
# a = "parasu"
# b = 10
# c = 10.0
# d = 10j
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(a)) == str
# print(type(b)) == int
# print(type(c)) == float
# print(type(d)) == complex
# print(isinstance(a , str)) 
# print(isinstance(b , int)) 
# print(isinstance(c , float)) 
# print(isinstance(d , complex)) 

# Casting a number str
# decade = str(1980)
# statement = " I like rock music from the " + decade + "s."
# print (statement)

# multi_line = '''  HI Welcome 
# pkreddark 
# Become a python dev..
# '''
# print(multi_line)

#sentence 
# sentance =  'I\' Am parasu \t tab line \n new line'
# print(sentance)

# # lower case
# sentance =  'I\' Am parasu \t tab line \n new line'
# print(sentance.lower())
# # uppar case 
# sentance =  'I\' Am parasu \t tab line \n new line'
# print(sentance.upper())
# # title first case
# sentance = 'I\' Am parasu \t tab line \n new line'
# print(sentance.title())
# replace
# print(sentance.replace('tab','subscribe'))
# # lenth how many litter in the sentance
# print(len(sentance))  
# # litter add 
# sentance = sentance +"test new litter add back side"
# sentance += " shotcut keyword add sentance"
# sentance ="   fornt side      " + sentance
# print(len(sentance)) 
# # backspase remove
# print(len(sentance.strip()))
# print(len(sentance.lstrip()))
# print(len(sentance.rstrip()))

# # Build a Menu
# title = "menu".upper()
# print(title.center(20,"="))
# print("Coffee".ljust(18,".") + "$1".rjust(4))
# print("Muffin".ljust(18,".") + "$2".rjust(4))
# print("Cheesecake".ljust(18,".") + "$3".rjust(4))
# print("")

# arria
# str = "HELLO"
# str[0] = "H"
# str[1] = "E"
# str[2] = "L"
# str[3] = "L"
# str[4] = "O"
# str[:]
# str[0:]
# str[1:]
# str[2:]
# str[3:]
# str[4:]
# str[:0]
# str[:1]
# str[:2]
# str[:3]
# str[:4]
# str[:5] 
# print(str[1:4])

# Some Methods return boolean data
# print(str.startswith("H"))
# print(str.endswith("O"))
# print(str.endswith("L"))
# boolean data type
# myver = True
# x = bool(False)
# print(type(x))
# print(isinstance(myver, bool))
# intiger data type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# float data type
# fol = 10.78
# print(type(fol))
# print(abs(fol))
# print(abs(fol * -1))
# print(round(fol, 1))

# # complex
# comp = 5+7j
# print(type(comp))
# print(comp.real)
# print(comp.imag)
# zipcode = "623526"
# zip = int(zipcode)
# print(type(zip))
# print(type(zipcode))

# import math
# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(fol))
# print(math.floor(fol))
# print(math.degrees(fol))

# input data type
# a = input("enter the name:")
# b = "your name :"
# print(type(a))
# print(b,a)

# # Game 
# import random
# import sys
# from enum import Enum


# class RPS(Enum):
#    rock = 1
#    paper = 2
#    scissors = 3



# Player_choice = input("Enter... \n1 For Rock \n2 for paper \n3 for Scissors: \n: ")
# player = int(Player_choice)
# computer = random.choice("123")
# choice_computer = int(computer)

# if player < 1 or player > 3:
#     sys.exit("You must enter 1,2, or 3.")
# if choice_computer < 1 or choice_computer > 3:
#     sys.exit("You must enter 1,2, or 3.")

# print("")
# print("")
# print("you chose "+ str(RPS(player)).replace('RPS.','') + ".")      
# print("python chose " + str(RPS(choice_computer)).replace('RPS.','') + ".")
# print("")
# if player == 1 and choice_computer == 3:
#     print("✨Win")
# elif player == 2 and choice_computer == 1:
#     print("✨Win")
# elif player == 3 and choice_computer == 2:
#     print("✨Win")
# elif player == choice_computer:
#     print("Tie Game!")
# else:
#     print("Lose!😁")


# list str

# grocery_list = ['apple','milk',"banana"]

# data = ['parasuraman','24',True]

# emptylist = []

# print('apple' in grocery_list)
# print(data[0])
# print(data[-1])
# print(data[0:2])
# print(grocery_list.index('milk'))
# print(len(data))
# grocery_list.append('test')
# print(grocery_list)
# grocery_list += ['orange']
# print(grocery_list)
# grocery_list.extend(['new','polo car'])
# print(grocery_list)
# grocery_list.extend(data)
# grocery_list.insert(0,'Mutton')
# print(grocery_list)
# grocery_list[2:2]=['onion','pepper']
# print(grocery_list)
# grocery_list[1:3]=['chilli','tomato']
# print(grocery_list)
# grocery_list.remove('24')
# print(grocery_list)
# print(grocery_list.pop())
# print(grocery_list)
# del grocery_list[0]
# print(grocery_list)
# grocery_list.sort()
# print(grocery_list)
# grocery_list.sort(key=str.lower)
# print(grocery_list)
# # del data
# # data.clear()

# # list int
# nums = [3, 2, 78, 1, 5]
# nums.reverse()
# print(nums)
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# nums = [1, 24, 48, 3, 5]
# print(sorted(nums,reverse=True))
# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]
# print('')
# print(numscopy)
# print(mycopy)
# mycopy.sort()
# print(mycopy)
# print(type(nums))

# # Tuples
# mytuples = tuple(('Dave', 42, True))
# anothertuple = (1,2,3,6,8,3,2,2)
# print(mytuples)
# print(type(anothertuple))
# newlist = list(mytuples)
# newlist.append('nali')
# print(newlist)
# newtuple = tuple(newlist)
# print(newtuple)
# (one, *two, hey) = anothertuple
# print(one)
# print(two)
# print(hey)
# print(anothertuple.count(2))
# print(anothertuple.count(3))

# # dictionaries
# car = { 

#     "brand": "Tesla",
#     "model": "Model_3_P",
#     "year" : 1964 ,
# }
# car2 = dict(brand="Tesla",model="Model_3_P")
# car3 =(car2.copy())
# print(car)
# print(car2)
# print(type(car))
# print(type(car2))
# print(len(car))
# print(len(car2))

# # Access items
# print(car["brand"])
# print(car.get("model"))

# # list all keys
# print(car.keys())
# print(car.values())

# # list of key/values pairs as tuples
# print(car.items())

# # verify a key exists
# print("model" in car)
# print("price" in car)

# # change values
# car["brand"] = "Nio"
# print(car)
# car.update({"price": "400000$"})
# print(car)
# car.update({"brand": "Tesla"})
# print(car)
# car ["Ev"]="Yes" 

# # Remove items
# print(car.pop("price"))
# print(car)
# print(car.popitem())  #Tuple
# print(car)

# # Delete and clear
# car ["Ev"]="Yes"
# del car["Ev"]
# print(car)
# car2.clear()
# print(car2)
# del car2
# print(car3)

# # create a reference
# car2 = car

# print("Bed Copy")
# print(car2)
# print("Bed Copy")
# print(car)
# car2["EV"] = "NO"
# print(car)

# # copy
# car2 = car.copy()
# car2["EV"] = "NO"
# print(car)
# print(car2)

# # or use the dict () constructor function
# car4 = dict(car)
# print(car4)

# # Nested dictionaries
# member1 = {
#     "name": "plant",
#     "instrument":"brend"

# }
# member2 = {

#     "name": "Page",
#     "instrument": "model"

# }
# bard = {
#     "member1": member1,
#     "member2": member2
# }
# print(member1)
# print(member2)
# print(bard)
# print(bard["member1"])
# print(bard["member1"]["name"])
# print(bard["member2"]["instrument"])

# # Sets
# nums = {1,2,3,4}
# nums2 = set((1,2,3,4))
# print(nums)
# print(nums2)
# print(type(nums2))
# print(len(nums2))

# # No duplicate allowed
# nums = {1,2,2,3}
# print(nums)

# # Ture is a dupe of 1, False is a dupe of zero
# nums = {1,True, 2,False, 3,4,0}
# print(nums)

# # check if a value is in a set
# print(2 in nums)

# # But You cannot refer to an element in the set with an index position or a key

# nums.add(8)
# print(nums)

# # Add element from one set to another 
# morenums = {5,6,7}
# nums.update(morenums)
# print(nums)

# # you can use updata with lists, tuples, and dictionaries, too.
# # merge two set to create a new set 
# one = {1,2,3}
# two = { 5,6,7}

# mynewset = one.union(two)
# print(mynewset)

# #  Keep only the duplicates
# one = {1,2,3}
# two = {2,3,4}
# one.intersection_update(two)
# print(one)

# # keep everything except the duplicates
# one = {1,2,3}
# two = {2,3,4}
# one.symmetric_difference_update(two)
# print(one)

# loop
# while loop
# # break
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# # continue
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         continue
#     i += 1

# i = 1
# while i < 6:
#     i += 1 # 2 ,3 ,4 etc...
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("i is no longer less than 10")  

# For loop
# fruits =[ "apple", "banana","mango"]
# for x in fruits:
#     print(x)

# fruits =[ "apple", "banana","mango"]
# for x in fruits:
#     if x == "banana":
#         break # continue
#     print(x)

# for x in "share":
#     print(x)

# for x in range(10):
#     print(x)

# for x in range(2,4):
#     print(x)

# for x in range(0, 101, 5): # 0 to 100 , 5 + 10 + 15 etc...
#     print(x)
# else:
#     print("Glad that\'s over!")

# name = ["parasuraman","kaviya","parthiban"]
# action = ["codes","eats","sleep"]
# for names in name:
#     for actions in action:
#         print(names +" "+ actions + ".")

# for actions in action:
#     for names in name:
#         print(names +" "+ actions + ".")
# Name = "parasuraman"
# age = 18 
# def another ():
#     global age
#     def greeting(name):
#         print(name)
#         print(age)
#     greeting("Share")
# another()

# # color scoop
# Name = "parasuraman"
# age = 18 
# def another ():
#     global age
#     color = "green"
#     def greeting(name):
#         print(name)
#         print(age)
#         print(color)
#     greeting("Share")
# another()

# # local scoop color
# Name = "parasuraman"
# age = 18 
# def another ():
#     global age
#     age += 2
#     color = "green"
#     def greeting(name):
#         color = "red"
#         print(name)
#         print(age)
#         print(color)
#     greeting("Share")
# another()

# # scoop nonlocal 
# Name = "parasuraman"
# age = 18 
# def another ():
#     global age
#     age += 2
#     color = "green"
#     def greeting(name):
#         nonlocal color
#         color = "red"
#         print(name)
#         print(age)
#         print(color)
#     greeting("Share")
# another()

# # F-Strings method

# # strings
# person = "parasuraman"
# coins = 3

# ######################
# # # Concatenating strings

# print("\n"+ person + " has "+ str(coins)+" coins left. ")

# ######################
# # Previous &s formatting
# massage = "\n %s has %s coins left." %(person,coins)
# print(massage)

# ######################
# # Previous string.format ()method

# massage = "\n{} has {} coins left.".format(person, coins)
# print(massage)

# massage = "\n{} has {} coins left.".format(coins, person)
# print(massage)

# massage = "\n{0} has {1} coins left.".format(coins, person)
# print(massage)

# massage = "\n{1} has {0} coins left.".format(coins, person)
# print(massage)

# massage = "\n{person} has {coins} coins left.".format(coins = coins, person= person)
# print(massage)

# massage = "\n{coins} has {person} coins left.".format(coins = coins, person= person)
# print(massage)
# # # dits and f - strings 
# player = {'person':'Dave','coins':3}
# massage = "\n{person} has {coins} coins left.".format(**player)
# print(massage)

# # ######################
# # # F-strings

# message = f"\n {person} has {coins}coins left."
# print(message)

# message = f"\n {person} has {2*5}coins left."
# print(message)

# message = f"\n {person.lower()} has {2*5}coins left."
# print(message)


# message = f"\n {player['person']} has {2*5}coins left."
# print(message)

# # ######################
# # # you can pass formatting options 

# num = 10 
# print(f"\n 2.25 times {num} is {2.25 * num:.2f}")

# for num in range(1 , 11):
#     print(f"\n 2.25 times {num} is {2.25 * num:.2f}")

# for num in range(1 , 11):
#     print(f"\n {num} divided by 4.52 is {num / 4.52:.2f}")

# for num in range(1 , 11):
#     print(f"\n {num} divided by 4.52 is {num / 4.52:.2%}")

# # #
# # modules for python import and from 

# import math

# print(math.pi)

# # import math
# from math import pi
# print(pi)

# import math
# from math import pi
# import random as rdm
# print(pi)

# # print(dir(rdm))
# for item in dir(rdm):
#     print(item)

# import rps7verions

# print (__name__)
# print (rps7verions.rps())
