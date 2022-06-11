print("level 1")

x = float(input('Вклад в банке: '))
y = float(input('Желаемая сумма: '))
p = float(input('Процентная ставка: '))

year = 0

while x < y:
    year_percent = x / 100 * p
    x += year_percent
    round(x)
    year += 1
    print(f"Год после открытия вклада: {year} Общая сумма: {round(x)}")

print(f"Через {year} лет, ваш вклад достигнет {y} и составит {round(x)}")

print("level2")

n = int(input('Число повторений: '))
count = 0
while count < n:
    print('for - частный случай цикла while')
    count += 1


print('level 3')
number = input('Введите число, для суммирования его чисел: ')

sum = 0
for i in number:
    sum += int(i)
print(sum)
