from functools import wraps

#decorators can be used to help enforce restrictions on certain args

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed!")
        return fn(*args, **kwargs)
    return wrapper





@ensure_no_kwargs
def greet(name):
    print(f"Hi there {name}")


print(greet("Tony"))