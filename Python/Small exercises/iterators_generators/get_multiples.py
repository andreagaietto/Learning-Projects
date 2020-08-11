def get_multiples(input_number=1, count=10):
    if count >= 0:
        for num in range(1, count+1):
            yield input_number * num
            count -= 1
        


default_multiples = get_multiples()
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))


