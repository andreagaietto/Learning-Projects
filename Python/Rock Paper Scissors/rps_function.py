from random import randint
computer_choice = None
play_again = "y"
computer_score = 0
player_score = 0
def counter(score_count):
    if score_count == "computer":
        print(f"Computer wins, computer chose {computer_choice}!\n")
        global computer_score
        computer_score += 1
    else:
        print(f"Player wins, computer chose {computer_choice}!\n")
        global player_score
        player_score += 1    

print("Rock...")
print("Paper...")
print("Scissors...")
while play_again == "y": 
    player = input("Make your move: ").lower()
    rand_num = randint(1, 3)
    
    if rand_num == 1:
        computer_choice = "rock"
    elif rand_num == 2:
        computer_choice = "paper"
    else:
        computer = "scissors"
    if player == computer_choice:
        print("It's a tie, computer chose " + computer_choice + "!\n")
    elif player == "rock":
        if computer_choice == "paper":
            counter("computer")
        else:
            counter("player")
    elif player == "paper":
        if computer == "rock":
            counter("player")
        else:
            counter("computer")
    elif player == "scissors":
        if computer == "rock":
            counter("computer")
        else:
            counter("player")
    else:
        print("Please enter a valid move.\n")
    print(f"The current score is:\n Computer: {computer_score}\n Player: {player_score}")
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == "n":
        print("Thanks for playing!")