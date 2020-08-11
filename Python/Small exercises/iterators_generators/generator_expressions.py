def nums():
    for num in range(1, 10):
        yield num

#the below is much more concise
g = (num for num in range(1, 10))
print(next(g))
print(next(g))
print(next(g))