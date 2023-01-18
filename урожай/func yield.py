def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


t1 = list(my_enumerate('1234567890', 1))
t2 = list(enumerate('1234567890', 1)) == t1
print(t2)


def my_filter(function, iterable):
    if function is None:
        function = bool
    for x in iterable:
        if function(x):
            yield x


t1 = list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == \
     list(my_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]))
t2 = list(filter(lambda a: a % 2 == 0, range(10 + 1))) == \
     list(my_filter(lambda a: a % 2 == 0, range(10 + 1)))
print(t1, t2)


def my_map(func, *args):
    count_item = len(args)
    min_len_obj = float('inf')
    for obj in args:
        if len(obj) < min_len_obj:
            min_len_obj = len(obj)
    for x in range(min_len_obj):
        if count_item > 1:
            temp_res = []
            for item in args:
                temp_res.append(item[x])
            yield func(temp_res)
        else:
            for item in args:
                yield func(item[x])


t1 = list(my_map(int, '1234567890'))
t2 = list(my_map(min, range(10), range(20, 30), range(25, 15, -1)))

print(list(map(int, '1234567890')) == t1)
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) == t2)


def my_range(start, stop=0, step=1):
    if stop == 0:
        stop, start = start, stop
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


t1 = list(my_range(10))
t2 = list(my_range(10, 20))
t3 = list(my_range(10, 20, 3))
t4 = list(my_range(20, 10, 3))
t5 = list(my_range(20, 10, -3))
t6 = list(my_range(20, 10))

print(list(range(10)) == t1)
print(list(range(10, 20)) == t2)
print(list(range(10, 20, 3)) == t3)
print(list(range(20, 10, 3)) == t4)
print(list(range(20, 10, -3)) == t5)
print(list(range(20, 10)) == t6)


def my_zip(*args):
    min_el = float('inf')
    for item in args:
        if len(item) < min_el:
            min_el = len(item)
    for index in list(range(min_el)):
        res_list = []
        for items in args:
            res_list.append(items[index])
        yield tuple(res_list)


t1 = list(my_zip(range(10), range(15), range(8)))
t2 = list(my_zip(range(10), range(15), []))
t3 = list(my_zip(range(10)))

print(list(zip(range(10), range(15), range(8))) == t1)
print(list(zip(range(10), range(15), [])) == t2)
print(list(zip(range(10))) == t3)
