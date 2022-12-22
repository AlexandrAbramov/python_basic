import functools
import sys

ENABLE_TRACE = True


def super_trace():
    def deco(func):
        @functools.wraps(func)
        def inner(*args, c, d):
            if ENABLE_TRACE:
                print(func.__name__, *args, c, d)
            return func(*args, c=3, d=4)

        return inner

    return deco


@super_trace()
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d


if __name__ == "__main__":
    print(test2(1, 2, c=3, d=4))

ENABLE_TRACE = False


def super_trace():
    def deco(func):
        @functools.wraps(func)
        def inner(*args, c, d):
            if ENABLE_TRACE:
                print(func.__name__, *args, c, d)
            return func(*args, c=3, d=4)

        return inner

    return deco


@super_trace()
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d


if __name__ == "__main__":
    print(test2(1, 2, c=3, d=4))