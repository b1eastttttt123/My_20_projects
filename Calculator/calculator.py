import sys


def operation_user(operation):
    match operation:
        case '+':
            return number_first_user + number_second_user
        case '-':
            return number_first_user - number_second_user
        case '*':
            return number_first_user * number_second_user
        case '/':
            if number_second_user == 0:
                return 'На ноль делить нельзя'
            return number_first_user / number_second_user
        case _:
            return None


try:
    number_first_user = float(input('Введите первое число: '))
    number_second_user = float(input('Введите второе число: '))
except ValueError:
    print('Error: нужно ввести цифру!')
    sys.exit(1)

operations = input('Введите символ операции: ')

results = operation_user(operations)

if results is None:
    print('Error: вы ввели недопустимый знак!')
else:
    print('Ответ:', number_first_user, operations, number_second_user, '=', results)
