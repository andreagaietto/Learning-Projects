print("Second Number Pattern ")
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end = "")
    print("")

choice = int(input("Give me a number "))
total_sum = 0
for x in range(1, choice + 1):
    total_sum += x
    x += 1
print(total_sum)


    
