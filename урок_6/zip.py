def my_zip(*args):
    res = []
    count_item = len(args)
    min_el = float('inf')
    for obj in args:
        if len(obj) < min_el:
            min_el = len(obj)
    for index in range(min_el):
        if count_item > 0:
            tmp = []
            for coll in args:
                tmp.append(coll[index])
            res.append(tuple(tmp))
    return res


print(list(zip(range(10), range(15), range(8))) == my_zip(range(10), range(15), range(8)))
print(list(zip(range(10), range(15), [])) == my_zip(range(10), range(15), []))
print(list(zip(range(10))) == my_zip(range(10)))