import functools
import sys

ENABLE_TRACE = True  # False


def super_trace(file=sys.stderr):
    def deco(func):
        @functools.wraps(func)
        def inner(a, b, c, d):
            if ENABLE_TRACE:
                print(func.__name__, a, b, c, d, file=file)
            return func(a=1, b=2, c=3, d=4)

        return inner

    return deco


@super_trace(file=sys.stderr)
def test3(*, a, b, c, d):
    return [a, b, c, d], a, str(b), float(c), d


if __name__ == "__main__":
    print(test3(a=1, b=2, c=3, d=4))

ENABLE_TRACE = False


def super_trace(file=sys.stderr):
    def deco(func):
        @functools.wraps(func)
        def inner(a, b, c, d,):
            if ENABLE_TRACE:
                print(func.__name__, a, b, c, d, file=file)
            return func(a=1, b=2, c=3, d=4)

        return inner

    return deco


@super_trace(file=sys.stderr)
def test3(*, a, b, c, d):
    return [a, b, c, d], a, str(b), float(c), d


if __name__ == "__main__":
    print(test3(a=1, b=2, c=3, d=4))