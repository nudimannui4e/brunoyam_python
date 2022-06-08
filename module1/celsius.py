#celsious = float(input("Введите температуру: "))
#fahrenheit = celsious * 1.8 + 32

for celsious in range(101):
	fahrenheit = celsious * 1.8 + 32
	print("%.0f" % celsious,"%.1f" % fahrenheit)