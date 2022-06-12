print('level 1')

from math import sqrt

def area(a, b, c):
    '''
    Функция нахождения площади треугольника
    '''
    p = (a + b + c) / 2
    s = sqrt(p * (p-a) * (p-b) * (p-c))

    print('Площадь треугольника:', format(s,".2f"))

#a = int(input('Сторона А? '))
#b = int(input('Сторона B? '))
#c = int(input('Сторона C? '))
#area(a,b,c)

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

#five_word(s)


print('level 3')

a_massiv = [56,9,11,2]
b_massiv = [3,81,5]

def max_number(array_input):
    for i in array_input:
        if i > array_input[i+1]:
            print(i)
    #print(''.join(sort_mas))

max_number(a_massiv)
