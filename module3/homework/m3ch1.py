print("level 1")

x = int(input('Вклад в банке: '))
y = int(input('Желаемая сумма: '))
p = int(input('Процентная ставка: '))

year = 0


while x < y:
    year_percent = round(x / 100 * p)
    x += year_percent
    year += 1
    print(f"Год после открытия вклада: {year} Общая сумма: {x}")

print(f"Через {year} лет, ваш вклад достигнет {y} и составит {x}")
