import random

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer":computer_choice}
    return choices
    
def check_win(player, computer):
    print (f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it is a tie"
        
        
    elif player == "rock":
        if computer == "scissors":
            return "you win"
        else:
            return "you loose"
        
        
    elif player == "paper":
        if computer == "scissors":
            return "you loose"
        else:
            return "you win"
        
        
    elif player == "scissors":
        if computer == "paper":
            return "you win"
        else:
            return "you loose"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
