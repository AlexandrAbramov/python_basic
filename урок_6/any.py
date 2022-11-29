def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False


b = any([]) == my_any([])
print(b)
b1 = ([0, 5, 0])
b2 = (['', (), {}])
b3 = my_any(b1), my_any(b2)
print(b3)
b1 = ([0, 5, 0])
b2 = ([0, ' ', 0])
b3 = my_any(b1), my_any(b2)
print(b3)
b1 = ([0, 0, 0])
b2 = ([(), '', []])
b3 = my_any(b1), my_any(b2)
print(b3)