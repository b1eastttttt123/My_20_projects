def celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


print('Единицы температуры: ')
print('')
print('1. Градус Цельсия')
print('2. Градус Фаренгейта')
print('3. Выключить программу')

while True:
    try:
        choice_temperature = int(input('\nВыберите единицу измерения температуры: '))

        match choice_temperature:
            case 1:
                write_temperature = float(input('Введите градус температуры в Цельсиях: '))
                result_fahrenheit = celsius_to_fahrenheit(write_temperature)
                print(f'\nОтвет: Градус Цельсия {write_temperature} равен Градус Фаренгейта = {result_fahrenheit}')
            case 2:
                write_temperature = float(input('Введите градус температуры в Фаренгейта: '))
                result_celsius = fahrenheit_to_celsius(write_temperature)
                print(f'\nОтвет: Градус Фаренгейта {write_temperature} равен Градус Цельсия = {result_celsius}')
            case 3:
                print('Программа выключена!')
                break
            case _:
                print(f'К сожалению, такой цифры не существует! - {choice_temperature}')

    except ValueError:
        print('Error: нужно вводить только цифры!')
