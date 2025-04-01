# # #importn
# # #Closure is a function having access to the scoop of its parent function after the parent function has returned

# def parent_function(person):
#     coins = 3
#     def play_game():
#         # nonlocal mens chagen velud
#         # global mens not chagen velud only see
#         nonlocal coins
#         coins -= 1
#         if coins > 1:
#             print("\n"+person+"has"+str(coins)+"coins left.")
#         elif coins == 1:
#             print("\n"+person+"has"+str(coins)+"coin left.")
#         else:
#             print("\n"+person+"is out of coins.")
#     return play_game
# tommy = parent_function("Tommy")
# jenny = parent_function("Jenny")
# tommy()
# jenny()

# #importn
# #Closure is a function having access to the scoop of its parent function after the parent function has returned

# def parent_function(person):
#     coins = 3
#     def play_game():
#         # nonlocal mens chagen velud
#         # global mens not chagen velud only see
#         nonlocal coins
#         coins -= 1
#         if coins > 1:
#             print("\n"+person+"has"+str(coins)+"coins left.")
#         elif coins == 1:
#             print("\n"+person+"has"+str(coins)+"coin left.")
#         else:
#             print("\n"+person+"is out of coins.")
#     return play_game
# tommy = parent_function("Tommy")
# jenny = parent_function("Jenny")
# tommy()
# jenny()
# tommy()
# jenny()
# tommy()


# #importn
# #Closure is a function having access to the scoop of its parent function after the parent function has returned

def parent_function(person,coins):
    # coins = 3
    def play_game():
        # nonlocal mens chagen velud
        # global mens not chagen velud only see
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n"+person+"has"+str(coins)+"coins left.")
        elif coins == 1:
            print("\n"+person+"has"+str(coins)+"coin left.")
        else:
            print("\n"+person+"is out of coins.")
    return play_game
tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)
tommy()
jenny()
tommy()
jenny()
tommy()
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
# Mutilplier of 3
times3 = make_multiplier_of(3)
# Mutilplier of 5
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(3))
print(times5(times3(2)))

