import random


def guessTheNumber(number_bot):
    while True:
        try:
            user_guess = input('Как думаешь какое число загадала Валькирия? (или введите "выход" для завершения) - ')
            if user_guess.lower() == 'выход':
                print('Спасибо за игру!')
                break

            user_guess = int(user_guess)

            if user_guess < number_bot:
                print(f'Хах, твое число - {user_guess} ниже моего, поэтому бери выше!')
            elif user_guess > number_bot:
                print(f'Хах, твое число - {user_guess} выше моего, поэтому бери ниже!')
            else:
                print(f'\nУраааааа, Ты нашел мое загаданное число - {number_bot}')
                break

        except ValueError:
            print('Error: нужно вводить только числа!')


print('Привет, мой друг!, Меня зовут - Бот Валькирия!')
print('Давай сыграем в игру "Угадай число"')
print('Я загадала число от 1 до 100, твоя задача отгадать!')
print('Поехали!\n')

number_bot = random.randint(1, 100)

guessTheNumber(number_bot)
