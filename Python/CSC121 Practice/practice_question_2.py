temp_list = []
num_hotter = 0
for x in range(5):
    temp = float(input("Enter a temperature: "))
    temp_list.append(temp)
print(f"Temperatures entered: {temp_list}")
print(f"Lowest temperature: {min(temp_list)}")
print(f"Highest temperature: {max(temp_list)}")
average_temp = (sum(temp_list)) / 5
print(f"Average temperature: {average_temp}")
for temp in temp_list:
    if temp > average_temp:
        num_hotter +=1
print(f"Num days hotter than average: {num_hotter}")
