a = [3, 10, 11, 2, 5]

def bubble_sort(a):
    n = len(a)

    for i in range(n - 1):
        for j in range (n - i -1):
            '''
            От большего к меньшему
            if a[j+1] > a[j]:
                a[j], a[j+1] = a[j+1], a[j]
            '''
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


print(a)
print(bubble_sort(a))