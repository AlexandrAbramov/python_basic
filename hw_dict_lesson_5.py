#  1. Зробити загальний словник.
dict_a = {'key_1': 'value_1',
          'key_2': 'value_2',
          'key_3': 'value_3',
          'key_4': 'value_4',
          'key_5': 'value_5'}

dict_b = {'key_6': 'value_6',
          'key_7': 'value_7',
          'key_8': 'value_8',
          'key_9': 'value_9',
          'key_10': 'value_10'}
dict_d = {}
dict_d.update(dict_a)
dict_d.update(dict_b)
print(dict_d)
#  2. Взяти ключі словника dict_a і значення словника dict_b і зробити загальний словник:
d1 = list(dict_a.keys())
d2 = list(dict_b.values())
res = dict(zip(d1, d2))
print(res)
#  3. Взяти значення словника dict_b і ключі словника dict_a і зробити загальний словник:
d1 = list(dict_a.keys())
d2 = list(dict_b.values())
res = dict(zip(d2, d1))
print(res)
#  4. Використовуючи результат з першого завдання res зробити словник,
#  де будуть тільки непарні числа в закінченнях ключей і значень
res = {'key_1': 'value_1', 'key_2': 'value_2',
       'key_3': 'value_3', 'key_4': 'value_4',
       'key_5': 'value_5', 'key_6': 'value_6',
       'key_7': 'value_7', 'key_8': 'value_8',
       'key_9': 'value_9', 'key_10': 'value_10'}
res1 = {}
for key, val in res.items():
    number = int(key.split('_')[-1])
    if number % 2 != 0:
        res1[key] = val
print(res1)
#  5. Створити словник де ключем буде ім'я словника dict_a або dict_b, а значенням
#  буде кількість пар-ключ значення які знаходяться в dict_a або dict_b зі словника dict_c
dict_a = {'key_1': 'value_1',
          'key_2': 'value_2',
          'key_3': 'value_3',
          'key_4': 'value_4',
          'key_5': 'value_5'
          }

dict_b = {'key_6': 'value_6',
          'key_7': 'value_7',
          'key_8': 'value_8',
          'key_9': 'value_9',
          'key_10': 'value_10'
          }
dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}
set_a = set(dict_a.items())
set_b = set(dict_b.items())
set_c = set(dict_c.items())
res2 = {
      'dict_a': len(set_a & set_c),
      'dict_b': len(set_b & set_c)
}
print(res2)
