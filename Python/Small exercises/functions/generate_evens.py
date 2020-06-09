def generate_evens():
    evens = []
    for i in range(1, 50):
        if i%2 == 0:
            evens.append(i)
    return evens

print(generate_evens())


