import functools
import sys

ENABLE_TRACE = True  # False


def super_trace():
    def deco(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if ENABLE_TRACE:
                print(func.__name__, *args, **kwargs, file=sys.stderr)
            return func(*args, **kwargs)

        return inner

    return deco


@super_trace()
def test5():
    return [1, 2, 3]

print(test5())
ENABLE_TRACE = False


def super_trace():
    def deco(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if ENABLE_TRACE:
                print(func.__name__, *args, **kwargs, file=sys.stdout)
            return func(*args, **kwargs)

        return inner

    return deco


@super_trace()
def test5():
    return [1, 2, 3]

print(test5())