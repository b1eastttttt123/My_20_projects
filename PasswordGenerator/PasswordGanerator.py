import random

print('Добро пожаловать в компанию Eniturse')

while True:
    print('\n1. Войти')
    print('2. Зарегистрироваться')

    your_choice = int(input('Введите цифру: '))

    match your_choice:
        case 1:
            print('\nВход')

            with open('logins_users.txt') as file:
                logins = file.read().splitlines()

            with open('passwords_users.txt') as file:
                passwords = file.read().splitlines()

            login = input('\nВведите Ваш логин: ')

            if login in logins:
                password = input('Введите ваш пароль: ')

                if password in passwords:
                    print('\nВы успешно вошли в учетную запись!')
                    break
                else:
                    print('Вы ввели пароль неправильно!')
            else:
                print('Неверный логин')

        case 2:
            print('\nРегистрация')

            login_user = input('Придумайте логин: ')

            with open('logins_users.txt', 'a') as file:
                file.write(login_user + '\n')


            while True:

                print('\nВыберите способ создания вашего пароля:')
                print('1. Сгенерировать пароль нейросетью')
                print('2. Создать свой личный пароль')

                choice_password = int(input('Выберите способ, как вы хотите создать пароль: '))

                match choice_password:
                    case 1:
                        print('\nПароль сгенерирован!')
                        text = [random.choice('qwertyuiop[]asdfghjkl;zxcvbnm,./123') for _ in range(10)]
                        print('')
                        print('Ваш пароль:', ''.join(text))

                        while True:

                            print('\nСохранить пароль?')
                            print('1. Да')
                            print('2. Нет')

                            yes_or_not = int(input('Выберите: '))

                            match yes_or_not:
                                case 1:
                                    print('\nВаш пароль успешно сохранен!')

                                    with open('passwords_users.txt', 'a') as file:
                                        file.write(''.join(text) + '\n')
                                    break
                                case 2:
                                    text = [random.choice('qwertyuiop[]asdfghjkl;zxcvbnm,./123') for _ in range(10)]
                                    print('')
                                    print('Ваш пароль:', ''.join(text))
                                case _:
                                    print('Error: неправильно ввели цифру!')
                        break

                    case 2:
                        password_user = input('\nНапишите ваш пароль: ')
                        repeat_password_user = input('Повторите ваш пароль: ')

                        if password_user == repeat_password_user:
                            with open('passwords_users.txt', 'a') as file:
                                file.write(password_user + '\n')
                            print('\nВаш пароль сохранен!')
                            break
                        else:
                            print('Пароли не совпадают!')

                    case _:
                        print('Error: неправильно ввели цифру!')

        case _:
            print('Error: неправильно ввели цифру!')

