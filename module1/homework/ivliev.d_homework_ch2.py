# level 1
import random
def level1():
	for i in range(1,6):
		print(str(i) + "-й набор чисел:")
		x = random.randint(1,5)
		y = random.randint(1,5)
		z = random.randint(1,5)
		print(x,y,z)

		print("Совпадения:")
		if (x == y and x == z):
			print(3)
		elif ((x == y) or (x == z) or (y == z)):
			print(2)
		else:
			print(0)
		print()
		i += 1

# level 2
def level2():
	print("Координаты начала:")
	x1 = int(input())
	y1 = int(input())
	print("Координаты предпологаемого хода:")
	x2 = int(input())
	y2 = int(input())

	if (x1 == x2) or (y1 == y2):
		print("YES")
	else:
		print("NO")


# level 3

def level3():
    # Переключатель, что пароль прошел проверку
    validate_pass = False
    # Счетчик строчных, больших букв
    flag_lower = 0
    flag_upper = 0
    password = str(input("Enter pass:\n> 8 symbols, Up+lowercase\n"))

    while validate_pass == False:
        if len(password) < 8:
            print("Symbols <8")
            password = str(input("Enter pass:\n> 8 symbols, Up+lowercase\n"))
        else:
            for element in password:
                if element.isupper() == True:
                    flag_upper += 1
                elif element.islower() == True:
                    flag_lower += 1
                else:
                    print("Password incorrect. Only Upper & Lower case")
                    password = str(input("Enter pass:\n> 8 symbols, Up+lowercase\n"))

        #debug Регистра
#        print("Кол-во строчных", flag_lower)
#        print("Кол-во заглавных", flag_upper)

        if (flag_upper > 0)  and (flag_lower > 0):
            print("Password is valid", password)
            validate_pass = True
        else:
            password = str(input("Enter pass:\n> 8 symbols, Up+lowercase\n"))

level1()
level2() 
level3()
