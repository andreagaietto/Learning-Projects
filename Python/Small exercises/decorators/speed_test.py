#speed test decorator
from time import time
from functools import wraps
def speed_test(fn):
    @wraps(fn)
    def wrapper(*args):
        start_time = time()
        result = fn(*args)
        end_time = time()
        print(f"Time Elasped: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums():
    return sum(x for x in range(100000))
print(sum_nums())
