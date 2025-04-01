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