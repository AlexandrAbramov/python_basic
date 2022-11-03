#  1. Отримати загальний set
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}
res = set_a.union(set_b,  set_c)
print(res)
#  2. Отримати різницю між set_a і set_b, set_b і set_c
res_a_b = set_a - set_b
res_b_c = set_b - set_c
res_a_c = set_a - set_c
print(res_a_b, res_b_c, res_a_c)
#  3. Отримати загальні елементи між set_a і set_b, set_b і set_c
res_a_b = set_a & set_b
res_b_c = set_b & set_c
res_a_c = set_a & set_c
print(res_a_b, res_b_c, res_a_c)
#  4. Перевірити чи є set {1, 2} підмножиною кожного set_a, set_b, set_c
set1 = {1, 2}
print(set1 <= set_a, set1 <= set_b, set1 <= set_c)
#  5. Використовуючи результат res з задачі 1 створити два set res_1, res_2
#  res_1 тільки парні, res_2 тільки непарні.
res.add(0)
res2 = set()
res1 = set()
for i in res:
    if i in range(0, 12, 2):
        continue
    res2.add(i)
for i in res:
    if i in range(1, 12, 2):
        continue
    res1.add(i)
print(res1, res2)