from random import randint
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif player == "rock":
        if computer == "paper":
            return "computer"
        else:
            return "player"
    elif player == "paper":
        if computer == "rock":
            return "player"
        else:
            return "computer"
    elif player == "scissors":
        if computer == "rock":
            return "computer"
        else:
            return "player"
    else:
        print("Please enter a valid move.\n")

print("Rock...")
print("Paper...")
print("Scissors...")

play_again = "y"
computer_score = 0
player_score = 0
while play_again == "y": 
    player_input = input("Make your move: ").lower()
    rand_num = randint(1, 3)
    
    if rand_num == 1:
        computer_input = "rock"
    elif rand_num == 2:
        computer_input = "paper"
    else:
        computer_input = "scissors"
    
    winner = determine_winner(player_input, computer_input)
    
    if winner == "player":
        print(f"Player wins, the computer chose {computer_input}.")
        player_score += 1
    elif winner == "computer":
        print(f"Computer wins, the computer chose {computer_input}.")
        computer_score += 1
    elif winner == "tie":
        print("Tie")
    
    print(f"The current score is:\n Computer: {computer_score}\n Player: {player_score}")
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == "n":
        print("Thanks for playing!")