n = 100

for i in range(1, n):
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c += 1
    if c == 0:
        print(i)
