from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == int:
                return fn(*args, **kwargs)
            else:
                return "Please only invoke with integers"
    return wrapper
    






@only_ints 
def add(x, y):
    return x + y


print(add(1, 2)) # 3
print(add("1", "2")) # "Please only invoke with integers."


"""def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner"""