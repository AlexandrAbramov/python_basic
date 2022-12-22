def my_map(func, *args):
    res = []
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
            res.append(func(temp_res))
        else:
            for item in args:
                res.append(func(item[x]))
    return res
print(list(map(int, '1234567890')) == my_map(int, '1234567890'))
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) ==
      my_map(min, range(10), range(20, 30), range(25, 15, -1)))