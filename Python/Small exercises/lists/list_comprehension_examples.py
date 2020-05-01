numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers)

number_list = [1, 2, 3, 4, 5]

doubled_number_list = [number * 2 for number in number_list]
print(doubled_number_list)

friends = ["ashley", "brad", "david"]
friend_caps = [friend[0].upper() + friend[1:] for friend in friends]

print(friend_caps)

times_ten = [num * 10 for num in range(1, 6)]
print(times_ten)

lean = [bool(val) for val in [0, [], ""]]
print(lean)

not_string = [1, 2, 3, 4, 5]
string_list = [str(value) for value in numbers]
print(string_list)

colors = ["red", "blue", "green", "yellow"]
color_upper = [color.upper() for color in colors]
print(color_upper)

with_vowels = "This is so much fun!"
joined = ''.join(char for char in with_vowels if char not in "aeiou")
print(joined)