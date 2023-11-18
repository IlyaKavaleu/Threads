import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'Func = {func.__name__} Time = {time.perf_counter() - start:0.2f}')
        return result
    return wrap
