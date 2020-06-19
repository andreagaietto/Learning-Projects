def intersection(list_one, list_two):
    list_three = [x for y in list_two for x in list_one if x == y]
    return list_three

intersection(["a", "b", "z"], ["x", "y", "z"])
