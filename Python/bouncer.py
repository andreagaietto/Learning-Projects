#ask for age
age = input("How old are you?: ")
if age != "":
    age = int(age)
#18-21 wristband
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
# 21+ drink, normal entry
    elif age >= 21:
        print("You can drink and enter normally.")
#too young, sorry
    else:
        print("Too young, sorry!")
else:
    print("Please enter an age!")
