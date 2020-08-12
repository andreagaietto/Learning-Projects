import random

def make_number_func(upper_range):
    def random_number():
        chosen_number = random.randint(0, upper_range)
        return chosen_number

    return random_number


why_me = make_number_func(100)
oh_god_why = make_number_func(1000)

print(why_me() + oh_god_why())