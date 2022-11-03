#  Задача 1.
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = list_a + list_b
print(list_c)
#  Задача 2.
res = [i for sublist in zip(list_a, list_b) for i in sublist]
print(res)
#  Задача 3.
list_c_a = []
list_c_b = []
for i in range(2, 5, 2):
    list_c_a.append(i)
    continue
for i in range(7, 10, 2):
    list_c_b.append(i)
    continue
print(list_c_a, list_c_b)
#  Задача 4.
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_c.reverse()
list_d = list_c
print(list_d)
#  Задача 5.
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
res = map(sum, zip(list_d, list_c))
print(list(res))
#  Задача 6.
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
list_f.sort(), list_f.remove(0), list_f.append(10)
res1 = list_f
res2 = list(reversed(res1))
print(res1, res2)
#  Задача 7.
res1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
res = [tuple(tup) for tup in zip(res1, res2)]
print(res)
