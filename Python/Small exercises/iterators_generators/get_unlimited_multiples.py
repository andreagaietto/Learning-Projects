def get_unlimited_multiples(user_choice=1):
    multiplier = 1
    while True:
        yield user_choice * multiplier
        multiplier += 1



sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])
