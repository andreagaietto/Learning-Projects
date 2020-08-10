#generator functions use yield instead of return. yield can be used multiple times. returns a generator object
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))