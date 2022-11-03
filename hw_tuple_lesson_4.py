#  Задача 1. Використовуючи tuple_a і tuple_b і tuple_c зробити загальний кортеж tuple_d
tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)
tuple_d = tuple_a + tuple_b + tuple_c
print(tuple_d)
#  Задача 2. Використовуючи tuple_d згенерувати кортеж res,
#  де буде кожен елемент це кортеж в якому:
# - першим елементом буде елемент з кортежу tuple_d
# - другим буде кількість елементів, що зустрічаються в кортежі tuple_d,
#  за умови що кількість елементів, що зустрічаються > 1
res = []
for i in tuple_d:
    if tuple_d.count(i) > 1:
        res.append((i, tuple_d.count(i)))
print(tuple(res))
#  Задача 3. Використовуючи tuple_d згенерувати кортеж res,
#  де буде кожен елемент це кортеж в якому:
# - першим елементом буде елемент з кортежу tuple_d
# - другим буде кортеж з індексами елементів які повторюється
#  Умова: кількість елементів, що повторюються повинно бути більше 1
res = []
elements = []
for element in tuple_d:
    count = tuple_d.count(element)
    if count > 1 and element not in elements:
        elements.append(element)
        indexes = []
        for index, item in enumerate(tuple_d):
            if item == element:
                indexes.append(index)
        res.append((element, (tuple(indexes))))
print(tuple(res))