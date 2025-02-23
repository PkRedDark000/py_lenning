# # scoop and def and closur and f-strngs game 
import random
import sys
from enum import Enum
game_count = 0
def rps():
    game_count = 0
    python_wins = 0
    player_wins = 0
    def play_rps():
        class RPS(Enum):
            rock = 1
            paper = 2
            scissors = 3
        Player_choice = input("Enter... \n1 For Rock \n2 for paper \n3 for Scissors: \nEnter the Number: ")
        if Player_choice not in ["1","2","3"]:
                print("You must Enter 1,2,3.")
                return play_rps()
                
        player = int(Player_choice)
        computer = random.choice("123")
        choice_computer = int(computer)

        print("")
        print("")
        print(f"you chose {str(RPS(player)).replace('RPS.','').title()}.")      
        print(f"python chose  {str(RPS(choice_computer)).replace('RPS.','').title()}.")
        print("")
        def game_play(player,choice_computer):
            nonlocal python_wins
            nonlocal player_wins
            if player == 1 and choice_computer == 3:
                player_wins += 1
                print( "✨Win")
            elif player == 2 and choice_computer == 1:
                player_wins += 1
                print ( "✨Win")
            elif player == 3 and choice_computer == 2:
                player_wins += 1
                print ("✨Win")
            elif player == choice_computer:
                print ("Tie Game!")
            else:
                python_wins += 1
                print ("Lose!😁")
        game_result = game_play(player,choice_computer)
        nonlocal game_count
        game_count += 1
        print(f"\nGame count :  {str(game_count)}")
        
        print(f"\nPlayer wins count : {str(player_wins)}")
        
        print(f"\nPython wins count : {str(python_wins)}")

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
        
    return play_rps()

if __name__ == "__main__":
    rps()
    
   

