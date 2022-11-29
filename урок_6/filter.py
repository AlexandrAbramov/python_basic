def my_filter(function, iterable):
    if function is None:
        function = bool
    for x in iterable:
        if function(x):
            yield x


a = list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == \
    list(my_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]))
a1 = list(filter(lambda a: a % 2 == 0, range(10+1))) == \
     list(my_filter(lambda a: a % 2 == 0, range(10+1)))
print(a, a1)