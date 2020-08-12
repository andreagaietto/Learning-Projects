from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if "role" in kwargs.keys() and "admin" in kwargs.values():
            return fn(*args, **kwargs)
        else:
            return "Unauthorized"
    return wrapper



@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody")) # "Unauthorized"
print(show_secrets(a="b")) # "Unauthorized"