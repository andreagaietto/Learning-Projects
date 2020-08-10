def yes_or_no():
    words = ["yes", "no"]
    count = 0
    while True:
        if count % 2 == 0:
            yield words[0]
        else:
            yield words[1]
        count += 1
            





gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
