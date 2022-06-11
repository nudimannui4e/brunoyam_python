l = [1, 2, 3, 1, 5, '123321', '3', '3']
l_uniq = []

for i in l:
    if i not in l_uniq:
        l_uniq.append(i)

print(l)
print(l_uniq)

print(list(set(l)))
