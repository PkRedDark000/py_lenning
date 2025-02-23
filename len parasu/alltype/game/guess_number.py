import random
import sys
from enum import Enum
game_count = 0
def rps(name="Playerone"):
    game_count = 0
    python_wins = 0
    player_wins = 0
    wins_person = 0
    
    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        Player_choice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3 : ")
        if Player_choice not in ["1","2","3"]:
                print(f"{name}, must Enter 1,2,3.")
                return play_rps()
                
        player = int(Player_choice)
        computer = random.choice("123")
        choice_computer = int(computer)

        print("")
        print("")
        print(f"{name} you chose {player}.")      
        print(f"I was thinking about the number {choice_computer}.")
        print("")
        def decide_Winner(player,choice_computer):
            nonlocal name
            nonlocal python_wins
            nonlocal player_wins
            nonlocal wins_person
            if player == choice_computer:
                player_wins += 1
                print (f"🎉{name}✨You Win!")
                wins_person = (game_count + player_wins - python_wins )
            else:
                python_wins += 1
                print (f"🐍Python Wins! \n{name}...Lose! the Game😁")
        game_result = decide_Winner(player,choice_computer)
        nonlocal game_count

        game_count += 1
        print(f"\nGame count :  {game_count}")
        
        print(f"\n{name}'s wins: {player_wins}")

        print (f"{wins_person /1:.2%}")
    
        print(f"\nPython wins : {python_wins}")

        print(f"\n Play again, {name} ?")

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
            sys.exit(f"Bye {name}!👋")
        
    return play_rps()

if __name__ == "__main__":
    import argparse

    perser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )
    perser.add_argument(
        "-n", "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game."
    )
    args = perser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()