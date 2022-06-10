# level 1
print("level 1")
value = (5 + 7 * 5 / 8) / (3**5)
print("значение выражения:", str(value))
print("значение выражения:", "%.4f" % value)

# level 2
print("level 2")

v = int(input("Скорость?"))
t = int(input("Время?"))
x = v * t % 109
print(f"Через {t} часов он остановился на {x} километре МКАД")

# level 3
print("level 3")
def without_if_else(x, y):
	print((x > y) * x + (y >= x) * y)

without_if_else(124.2, -2)
without_if_else(-9.3, -163.5)
without_if_else(float(input('X:')),
				float(input('Y:')))
