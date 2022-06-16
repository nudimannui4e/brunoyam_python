# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

"""
Бинарный поиск - это поиск элемента в отсортированном(!) массиве
Примерная схема работы:
    Массив делится на 2 равные части(примерно)
    Искомый элемент сравнивается с границами (от середины) этих массивов
    Если элемент больше правой или меньше левой части - такого элемента в массиве нет.
    Должно всегда соблюдаться условие:
        left <= X < right

    Очень сильно похоже на игру - угадай число.
"""


def binary_search_recursion(my_list, x, start, stop):
    if start > stop:
        # Если start > stop - значит числа нет в массиве
        return False
    else:
        midle = (start + stop) // 2
        if x == my_list[midle]:
            return midle
        elif x < my_list[midle]:
            return binary_search_recursion(my_list, x, start, midle - 1)
        else:
            return binary_search_recursion(my_list, x, midle + 1, stop)


# Генерируется отсортированный массив нечетных чисел
#my_list = [x for x in range(1, 51, 2)]

# Второй вариант - просто отсортированный массив
my_list = [1, 3, 22, 25, 27, 35, 50, 57, 78, 99]

# Число, которое нужно найти
x = 22

start = 0
stop = len(my_list)

index = binary_search_recursion(my_list, x, start, stop)

if index is False:
    print(f"Item {x} not found.")
else:
    print(f"Item {x} found at index: {index}")