import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds.")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(1)  # Simulate a slow task
    return a + b

print(slow_add(3, 4))