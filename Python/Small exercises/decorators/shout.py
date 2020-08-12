#accept a flexible number of arguments


def shout(fn):
    def wrapper(*args):
        return fn(*args).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}"

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

print(greet("Todd"))
print(order("salad", "tofu"))