import time
from functools import wraps
import logging


# How long a process takes to run

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to complete")
        return result

    return wrapper


# retry also has a popular library to cover: https://github.com/jd/tenacity
def retry(max_tries=3, delay_seconds=1):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    time.sleep(delay_seconds)

        return wrapper_retry

    return decorator_retry


# cache
# refer to system defined @lru_cache (from functools)

# logging

logging.basicConfig(level=logging.INFO)


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing{func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result

    return wrapper
