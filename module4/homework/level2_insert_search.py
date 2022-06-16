# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

"""
Алгоритм сортировки вставками. Крайне не эффективный для больших массивов.
Чем больше элементов, тем дольше он работает.

"""


def insertion_sort(array):
    # начинаем проходить со второго элемента (1)
    # т.к. 1-ый не с чем сравнивать
    for i in range(1, len(array)):
        # key - индекс массива
        key = array[i]
        # j - сравнение элемента с тем, что левее
        j = i - 1
        # Пока i не переместился в начало, и  i индекс меньше j индекса элемента
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


arr = [12, 11, 13, 5, 6]
print(f"Original array: {arr}")
sorted_arr = insertion_sort(arr)
print(f"Sorted array: {sorted_arr}")
