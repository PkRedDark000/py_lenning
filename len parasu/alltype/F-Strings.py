# # # strings
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



