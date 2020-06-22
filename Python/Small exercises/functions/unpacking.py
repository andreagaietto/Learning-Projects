def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

nums = (1, 2, 4, 5, 6)
sum_all_values(*nums)
#works with lists too


#for dictionaries:
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

# error if    display_names(names)

display_names(**names)


def add_and_multiply_numbers(a, b, c):
    print(a + b * c)

data = dict(a=1, b=2, c=3)

add_and_multiply_numbers(**data)
