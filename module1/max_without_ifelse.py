x1 = int(input("Число 1:"))
x2 = int(input("Число 2:"))
max1 = (x1 > x2) * x1 + (x2 >= x1) * x2
print("Max: ", max1)