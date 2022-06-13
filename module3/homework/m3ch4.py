import json
import os.path

'''
Закоменченный код запускается при первом старте
Позже добавлю проверку - есть ли такой файл
Если нет - создать
Если есть - дальше без этого куска кода
UPD - перенес в самый низ, в главный цикл While
'''

def register(login, passwd):
    with open('user_creds.json', 'r') as f:
        data_user = json.load(f)

    if login not in data_user.keys():
        data_user[login] = passwd
        with open('user_creds.json', 'w') as f:
            json.dump(data_user, f)
    else:
        print(f'User with login {login} exist')


def login_function(login, passwd):
    with open('user_creds.json', 'r') as f:
        data_user = json.load(f)
    if login in data_user.keys():
        if passwd != data_user.get(login):
            print('Пароль не подходит.\n')
        else:
            print('Успешный вход!\n')
    else:
        print('Такого логина нет')
        q1 = input('Желаете зарегистрироваться?(y/n)\n')
        if q1.lower() == 'y':
            register(login,passwd)


while True:
    checkin = input('Stop?(yes)').lower()
    if checkin == 'yes':
        break
    else:
        check_file = os.path.exists('user_creds.json')
        if check_file:
            action = input('Регистрация(1), вход(2)')
            if action == '1':
                login = input('Введите логин: ')
                passwd = input('Введите пароль: ')
                register(login, passwd)
            elif action == '2':
                login = input('Введите логин: ')
                passwd = input('Введите пароль: ')
                login_function(login, passwd)
        else:
            data_user = {
                'test_login': 'test_pass',
                'demo_user': 'demo_pass',
            }

            with open('user_creds.json', 'w') as f:
                json.dump(data_user, f)

            print('БД отсутствует. Пройдите регистрацию, для ее создания:\n')
            login = input('Введите логин: ')
            passwd = input('Введите пароль: ')
            register(login, passwd)