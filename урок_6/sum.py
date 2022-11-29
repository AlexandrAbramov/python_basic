def my_sum(iterable):
    start = 0
    for element in iterable:
        start += element
    return start


a = sum(range(10)) == my_sum(range(10))
print(a)
a1 = sum([]) == my_sum([])
print(a1)
