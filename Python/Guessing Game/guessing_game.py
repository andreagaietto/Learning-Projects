import random

decision = "y"
while decision == "y":
    random_number = random.randint(1, 10)
    choice = None
    while choice != random_number:
        choice = int(input("Guess a number between 1 and 10: "))    
        if choice < random_number:
            print("Too low, try again!")    
        else:
            print("Too high, try again!")
    print(f"You guessed it! You win! The computer chose {random_number}.")    
    decision = input("Do you want to keep playing? (y/n) ")

