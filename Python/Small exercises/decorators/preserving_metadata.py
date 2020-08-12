from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I am a wrapper function"""
        print(f"You are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """Adds two numbers together"""
    return x + y

print(add(10,30))
#gives info for the wrapper function, not the add function, without functools:
print(add.__doc__)
print(add.__name__)

#importing functools and wraps and placing @wraps decorator helps solve this