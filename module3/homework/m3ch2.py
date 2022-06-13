print('level 1')
l = [1, 4, 1, 6, "hello", "a", 5, "hello", 4, "dog", "cat", "dog"]
repeat = []

for i in l:
    if l.count(i) > 1:
        repeat.append(i)
print(f'Исходный список:\n{l}')
print(f'Найденные повторяющиеся элементы:\n{repeat}')
print('Найденные повторы, выведенные по одному:')
set_repeat = set(repeat)
print(*set_repeat, sep=", ")

print('\nlevel 2')

from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print(m)
# 1-ый способ
print(max(map(max,m)))

# 2-ой способ
_max = m[0][0]
for row in m:
    if _max < max(row):
        _max = max(row)

print(_max)
    

print('level3')
d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
new_d = {}
print(f'Исходный словарь: {d}')
for key, value in d.items():
    print(key, d[key])
    new_d[value] = key

print(f'Новый словарь: {new_d}')
