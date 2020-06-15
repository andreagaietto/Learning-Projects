democrat_won = 0
republican_won = 0
democrat_percent = 0
republican_percent = 0
for x in range(1, 6):
    print(f"Debate {x}:")
    democrat_percent = int(input("What percentage of people think the Democrat's candidate has won? "))
    republican_percent = int(input("What percentage of people think the Republican's candidate has won? "))
    if democrat_percent > republican_percent + 3:
        print("Democrat's candidate has won this debate\n")
        democrat_won += 1
    elif republican_percent > democrat_percent + 3:
        print("Republican's candidate has won this debate\n")
        republican_won += 1
    else:
        print("It is statistically a tie\n")
print(f"Number of debates the dems have won: {democrat_won}")
print(f"Number of debates the repubs have won {republican_won}")
if democrat_won > republican_won:
    print("The democrat candidate has won more debates.")
elif democrat_won < republican_won:
    print("The republican candidate has won more debates.")
else:
    print("The two candidates have won the same number of debates")




