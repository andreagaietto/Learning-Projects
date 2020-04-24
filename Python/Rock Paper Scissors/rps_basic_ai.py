from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Make your move: ").lower()
rand_num = randint(1, 3)

if rand_num == 1:
    computer = "rock"
elif rand_num == 2:
    computer = "paper"
else:
     computer = "scissors"

if player == computer:
    print("It's a tie, computer chose " + computer + "!")
elif player == "rock":
	if computer == "paper":
		print("Computer wins, computer chose " + computer + "!")
	else:
		print("Player wins, computer chose " + computer + "!")
elif player == "paper":
	if computer == "rock":
		print("Player wins, computer chose " + computer + "!")
	else:
		print("Computer wins, computer chose " + computer + "!")
elif player == "scissors":
	if computer == "rock":
		print("Computer wins, computer chose " + computer + "!")
	else:
		print("Player wins, computer chose " + computer + "!")
else:
	print("Please enter a valid move.")