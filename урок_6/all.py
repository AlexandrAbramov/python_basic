def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


a = all([]) == my_all([])
a1 = all([True, False]) == my_all([True, False])
a2 = all([True, True]) == my_all([True, True])
a3 = all([False, False]) == my_all([False, False])
print(a, a1, a2, a3)
a1 = (['11', 7, 8])
a2 = ([1, 5, ''])
a3 = my_all(a1), my_all(a2)
print(a3)
a1 = (['11', 7, 8])
a2 = ([1, 5, ' '])
a3 = my_all(a1), my_all(a2)
print(a3)
a1 = (['11', 0, 8])
a2 = ([1, 5, ''])
a3 = my_all(a1), my_all(a2)
print(a3)