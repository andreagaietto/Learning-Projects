with open('names.txt', 'r') as f:
    myNames = [line.strip() for line in f]
    for name in myNames:
        count = name.upper().count("A")
        print(f"{name} has {count} occurances of a.")