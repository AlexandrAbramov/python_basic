def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


a1 = list(my_enumerate('1234567890', 1))
print(a1)
a2 = list(enumerate('1234567890', 1)) == a1
print(a2)