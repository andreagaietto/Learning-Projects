list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for x in list1:
    if x > 150:
        break
    elif x%5 == 0:
        print(x)
    