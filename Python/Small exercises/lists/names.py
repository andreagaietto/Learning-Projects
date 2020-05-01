names = ["John", "James", "Aaron", "Andrea", "Joesph", "Amy", "George", "Neil", "Neal", "Arnold"]
for name in names:
    if name[0] == "A":
        print(f"{name} has an A at the beginning.")
    elif "a" in name:
        print(f"{name} has an a present somewhere in it.")
    else:
        print(f"{name} does not have any a's.")
    