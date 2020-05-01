answer_2 = [x[::-1].lower() for x in ["Elie", "Tim", "Matt"]]
print(answer_2)

answer_1 = [x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]]
print(answer_1)

range_100 = [x for x in range(1, 101) if x % 12 == 0]
print(range_100)

answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)