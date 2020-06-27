nums = [2, 4, 6, 8, 10]

doubles = list(map(lambda x: x*2, nums))

print(doubles)



people = ["Darcy", "Christina", "Dana", "Annabel"]

upper = list(map(lambda name: name.upper(), people))

print(upper)

names = [
    {'first' : 'Rusty', 'last' : 'Steele'},
    {'first' : 'Colt', 'last' : 'Steele'},
    {'first' : 'Blue', 'last' : 'Steele'},
]

first_names = list(map(lambda x: x['first'], names))
print(first_names)

def decrement_list(my_list):
    list_modified = list(map(lambda x: x - 1, my_list))
    return list_modified

print(decrement_list([1, 2, 3]))