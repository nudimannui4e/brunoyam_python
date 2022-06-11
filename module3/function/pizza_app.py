import json

#data_pizza = {
#        'margarita' : 400,
#        'carbonara' : 500,
#        }
#with open('pizza.json', 'w') as f:
#    json.dump(data_pizza, f)
'''
Инициация файла. Код выше - запускается 1 раз
'''

def add_pizza(name, price):
    with open('pizza.json', 'r') as f:
        data_pizza = json.load(f)
    if name not in data_pizza.keys():
        data_pizza[name] = price
        with open('pizza.json', 'w') as f:
            json.dump(data_pizza, f)
    else:
        print('Pizza already exist')


def del_pizza(name):
    with open('pizza.json', 'r') as f:
        data_pizza = json.load(f)
    if name in data_pizza.keys():
        del data_pizza[name]
        with open('pizza.json', 'w') as f:
            json.dump(data_pizza, f)
    else:
        print('Pizza not exist')


def order_pizza():
    with open('pizza.json', 'r') as f:
        data_pizza = json.load(f)
    order = []
    cost = 0
    while True:
        q1 = input('Continue? (yes | no)')
        if q1.lower() == 'no':
            break
        pizza_name = input('Pizza name?').lower()
        if pizza_name in data_pizza.keys():
            order.append(pizza_name)
            cost += data_pizza[pizza_name]
            print('Pizza added')
    return {'order' : order, 'cost': cost}


while True:
    break_point = input('Stop?').lower()
    if break_point == 'yes':
        break
    chose_role = input('Chose role:')
    if chose_role.lower() == 'user':
        print(order_pizza())
    else:
        q2 = input('Add or delete?').lower()
        if q2 == 'delete':
            del_pizza(input('Pizza name?'))
        elif q2 == 'add':
            add_pizza(input('Pizza name?').lower(), int(input('Price')))

