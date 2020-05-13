numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

example = {num: num**2 for num in [1, 2, 3, 4, 5]}
print(example)

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)

num_list = [1,2,3,4]
other_example = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(other_example)