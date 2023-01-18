import functools
import sys

ENABLE_TRACE = True  # False


def super_trace(file=sys.stderr):
    def deco(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if ENABLE_TRACE:
                print(func.__name__, *args, **kwargs, file=file)
            return func(*args, **kwargs)

        return inner

    return deco


@super_trace(file=sys.stderr)
def test1(a, b, c):
    return[a, b, c], a, str(b), float(c)


if __name__ == "__main__":
    print(test1(1, 2, 3))


ENABLE_TRACE = False


def super_trace(file=sys.stderr):
    def deco(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if ENABLE_TRACE:
                print(func.__name__, *args, **kwargs, file=file)
            return func(*args, **kwargs)

        return inner

    return deco


@super_trace(file=sys.stderr)
def test1(a, b, c):
    return[a, b, c], a, str(b), float(c)


if __name__ == "__main__":
    print(test1(1, 2, 3))