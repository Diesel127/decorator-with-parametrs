from functools import wraps
from typing import Callable
from random import randint

def decorator(exceptions: list[tuple[type[Exception], Callable[[Exception], None]]]):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for exc_type, handler in exceptions:
                    if isinstance(e, exc_type):
                        handler(e)
                        return None
                raise
        return wrapper
    return outer


def bar(e):
    print("1")


@decorator([
    (KeyError, bar),
    (IndexError, lambda e: print("2"))
])
def foo():
    random_num = randint(1, 3)
    if random_num == 1:
        raise KeyError()
    elif random_num == 2:
        raise IndexError()
    else:
        print("3")


foo()
