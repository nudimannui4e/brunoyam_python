print('level 1')
l = [1, 4, 1, 6, "hello", "a", 5, "hello", 4, "dog", "cat", "dog"]
repeat = []

for i in l:
    if l.count(i) > 1:
        repeat.append(i)
print(f'Исходный список:\n{l}')
print(f'Найденные повторяющиеся элементы:\n{repeat}')
