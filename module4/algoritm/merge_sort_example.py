a = [4, 5, 6, 10, 1, 3]


def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        # left = [4, 5, 6]
        left = merge_sort(a[:median])
        # right = [10, 1, 3]
        right = merge_sort(a[median:])
        return merge(left, right)


def merge(left, right):
    res = []
    # Указатели\индексы массивов
    i,j = 0,0

    while i < len(left) and j < len(right):
        '''
        Пока не пройдем все элементы left[], right[]
        '''
        if left[i] < right[j]:
            '''
            Условие выше - если изменить, будет сортировка от большего к меньшему
            Если левый меньше правого,
            перемещаем элемент в лево,
            и переходим к след элементу (увеличиваем i)
            '''
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    '''
    Дальше, нужно соединить эти массивы
    Пробегаемся по массиву left, и присоединяем его элементы к
    массиву, что получился из кода выше
    
    И так же, по массиву rigth
    '''

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


print(a)
print(merge_sort(a))
