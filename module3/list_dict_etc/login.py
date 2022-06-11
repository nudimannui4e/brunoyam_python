data = {'test_login': 'test_pass'}
login = True
secret_info = '42'

while login:
    q1 = input('Вход(1), регистрация(2), выход(3)\n')
    if q1.lower() == 'вход' or q1 == '1':
        log = input('Введите логин: ')
        passwd = input('Введите пароль: ')

        if log in data.keys():
            if data[log] == passwd:
                print('Успешный вход.')
                print(secret_info)
        else:
            print('Неверный логин.')
    elif q1.lower() == 'регистрация' or q1 == '2':
        log = input('Введите логин: ')
        passwd = input('Введите пароль: ')
        if log in data.keys():
            print('Логин занят.')
        else:
            data[log] = passwd
            print('Регистрация завершена')
    elif q1.lower() == 'выход' or q1 == '3':
        print('Bye Bye')
        login = False
