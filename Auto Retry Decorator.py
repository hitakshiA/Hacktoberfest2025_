import time
import functools

def retry(times=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i < times - 1:
                        time.sleep(delay)
                    else:
                        raise e
        return wrapper
    return decorator

@retry(times=5, delay=2)
def unstable_task():
    if time.time() % 2 < 1:
        raise Exception("Random failure")
    print("Task succeeded")

unstable_task()
