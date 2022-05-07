from functools import wraps
import time

def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.perf_counter()

        result = func(*args, **kargs)

        elapsed_time = time.perf_counter() - start

        print("{} ms in {}".format(elapsed_time*1000, func.__name__))
        return result
    return wrapper