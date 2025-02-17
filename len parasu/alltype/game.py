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

# game and loopes
# Game 
# import random
# import sys
# from enum import Enum


# class RPS(Enum):
#    rock = 1
#    paper = 2
#    scissors = 3

# play_again = True
# while play_again:


#     Player_choice = input("Enter... \n1 For Rock \n2 for paper \n3 for Scissors: \n: ")
#     player = int(Player_choice)
#     computer = random.choice("123")
#     choice_computer = int(computer)

#     if player < 1 or player > 3:
#         sys.exit("You must enter 1,2, or 3.")
#     if choice_computer < 1 or choice_computer > 3:
#         sys.exit("You must enter 1,2, or 3.")

#     print("")
#     print("")
#     print("you chose "+ str(RPS(player)).replace('RPS.','') + ".")      
#     print("python chose " + str(RPS(choice_computer)).replace('RPS.','') + ".")
#     print("")
#     if player == 1 and choice_computer == 3:
#         print("✨Win")
#     elif player == 2 and choice_computer == 1:
#         print("✨Win")
#     elif player == 3 and choice_computer == 2:
#         print("✨Win")
#     elif player == choice_computer:
#         print("Tie Game!")
#     else:
#         print("Lose!😁")
#     play_again = input("\nplay again? \nY for Yes or \nQ to Quit \n\n")

#     if play_again.lower() == "y":
#         continue
#     else:
#         print("\n🎉✨🎉✨🎉")
#         print("Thank you for playing!\n")
#         play_again = False
#     sys.exit("Bye!👋")

# # scoop def game 
import random
import sys
from enum import Enum
game_count = 0

def play_rps():
    class RPS(Enum):
        rock = 1
        paper = 2
        scissors = 3
    Player_choice = input("Enter... \n1 For Rock \n2 for paper \n3 for Scissors: \n: ")
    if Player_choice not in ["1","2","3"]:
            print("You must Enter 1,2,3.")
            return play_rps()
            
    player = int(Player_choice)
    computer = random.choice("123")
    choice_computer = int(computer)

    print("")
    print("")
    print("you chose "+ str(RPS(player)).replace('RPS.','') + ".")      
    print("python chose " + str(RPS(choice_computer)).replace('RPS.','') + ".")
    print("")
    def game_play(player,choice_computer):
        if player == 1 and choice_computer == 3:
            print("✨Win")
        elif player == 2 and choice_computer == 1:
            print("✨Win")
        elif player == 3 and choice_computer == 2:
            print("✨Win")
        elif player == choice_computer:
            print("Tie Game!")
        else:
            print("Lose!😁")
    game_result = game_play(player,choice_computer)
    global game_count
    game_count += 1
    print("Game count :" + str(game_count))
    print("\n Play again?")

    while True:
        play_again = input ("\nY for Yes or \nQ to Quit ")
        if play_again.lower() not in ["y","q"]:
            continue
        else:
            break
    if play_again.lower() == "y":
        return play_rps()
    else:
        print("\n🎉✨🎉✨🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye!👋")
    
play_rps()