import random
game=["rock","paper",'scissors']
player_choice=input("enter ur choice rock,paper,scissors:")
computer_choice=random.choice(game)
print("computer_choice is:",computer_choice)
def wins():
    choices={player_choice:"player",computer_choice:"computer"}
 
    beats={"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if player_choice==computer_choice:
      return "tie"
    elif beats[player_choice]==computer_choice:
        return print(choices[player_choice]+" won")
    else:
        return print(choices[computer_choice]+" won")
    

choices=wins()





    