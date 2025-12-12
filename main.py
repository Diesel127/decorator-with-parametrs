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


def bar():
    print("1")


@decorator([
    (KeyError, bar),
    (IndexError, lambda e: print("2"))
])
def foo():
    if randint(1, 2) == 1:
        raise KeyError("bar")
    else:
        raise IndexError()


foo()
