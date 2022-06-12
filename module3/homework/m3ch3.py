print('level 1')

from math import sqrt

def area(a, b, c):
    '''
    Функция нахождения площади треугольника
    '''
    p = (a + b + c) / 2
    s = sqrt(p * (p-a) * (p-b) * (p-c))

    print('Площадь треугольника:', format(s,".2f"))

a = int(input('Сторона А? '))
b = int(input('Сторона B? '))
c = int(input('Сторона C? '))
area(a,b,c)

print('level 2')

s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

print(f'Исходный текст:\n {s}\n')

# Фильтр знаков препинания
symbols = ['.',',','-','...',':','!','?']


def five_word(string):
    '''
    Первый цикл убирает знаки препинания
    Второй - режет строку на словарь (разделитель пробел),
    и вытаскивает в новый словарь то, что по длине меньше 5 символов
    '''

    s_clean = ''
    dict_five = []
    
    for char in string:
        if char not in symbols:
           s_clean += char
    
    for i in s_clean.split():
        if len(i) < 5:
            dict_five.append(i)

    print(f'Слова, меньше 5 символов:\n{dict_five}\n')

    clear_string = ' '.join(dict_five)
    print(f'Чистый вывод слов, меньше 5 символов:\n{clear_string}\n')

five_word(s)


print('level 3')

a_array = [56,9,11,2]
b_array = [3,81,5]

def max_number(array_input):

    '''
    Примерный смысл такой:
    создается 2 массива - 1 для максимальных чисел
    2-ой для минимальный

    Дальше, если длина числа больше 1, то такие числа сравниваются в лоб
    '''
    min_array = []
    max_array = []
    final_array = []
    # раскидываются числа до 9 в 1 массив, 
    # двузначные и больше - во второй
    for element in array_input:
        if len(str(element)) > 1:
            max_array.append(element)
        else:
            min_array.append(element)

    min_array.sort(reverse=True)
    max_array.sort(reverse=True)
    print(max_array, min_array)
    for i in max_array:
        for j in min_array:
            print(i, j)
            if (i // 10) > j:
                if i not in final_array:
                    final_array.append(i)
            elif j > (i // 10):
                if j not in final_array:
                    final_array.append(j)
    
    print(final_array)

max_number(a_array)
max_number(b_array)
