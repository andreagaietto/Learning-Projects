from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

play_again = "y"
computer_score = 0
player_score = 0
while play_again == "y": 
    player = input("Make your move: ").lower()
    rand_num = randint(1, 3)
    
    if rand_num == 1:
        computer = "rock"
    elif rand_num == 2:
        computer = "paper"
    else:
        computer = "scissors"
    if player == computer:
        print("It's a tie, computer chose " + computer + "!\n")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins, computer chose " + computer + "!\n")
            computer_score += 1
        else:
            print("Player wins, computer chose " + computer + "!\n")
            player_score += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins, computer chose " + computer + "!\n")
            player_score += 1
        else:
            print("Computer wins, computer chose " + computer + "!\n")
            computer_score += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins, computer chose " + computer + "!\n")
            computer_score += 1
        else:
            print("Player wins, computer chose " + computer + "!\n")
            player_score += 1
    else:
        print("Please enter a valid move.\n")
    print(f"The current score is:\n Computer: {computer_score}\n Player: {player_score}")
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == "n":
        print("Thanks for playing!")