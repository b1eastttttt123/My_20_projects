from datetime import datetime
import pytz

vladivostok_tz = pytz.timezone('Asia/Vladivostok')

current_time_vladivostok = datetime.now(vladivostok_tz)

print('Сегодня -', current_time_vladivostok.strftime('%Y-%m-%d %H:%M:%S'))

tasks = []


def display_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print('\nВаши задачи:\n')
        for index, task in enumerate(tasks, start=1):
            print(f"{index} - {task}")


while True:
    print('\nВыберите функцию: \n')
    print('1. Добавить задачу')
    print('2. Редактировать задачу')
    print('3. Удалить задачу')
    print('4. Посмотреть задачи')
    print('5. Закрыть программу')

    try:
        choice = int(input('\nВведите номер функции: '))
    except ValueError:
        print("Пожалуйста, введите число.")
        continue

    match choice:
        case 1:
            add_task = input('Введите вашу задачу и нажмите на ENTER: ')
            tasks.append(add_task)
            print('Задача добавлена!')

        case 2:
            display_tasks()
            if tasks:
                try:
                    edit_task = int(input('\nВыберите цифру под которой будем изменять задачу: '))
                    if 1 <= edit_task <= len(tasks):
                        task_user = input('\nВведите новую задачу: ')
                        tasks[edit_task - 1] = task_user
                        print('Задача обновлена!')
                    else:
                        print('Неверный номер задачи.')
                except ValueError:
                    print("Пожалуйста, введите число.")

        case 3:
            display_tasks()
            if tasks:
                try:
                    delete_task = int(input('Введите цифру задачи, которую хотите удалить: '))
                    if 1 <= delete_task <= len(tasks):
                        tasks.pop(delete_task - 1)
                        print('Задача удалена!')
                    else:
                        print('Неверный номер задачи.')
                except ValueError:
                    print("Пожалуйста, введите число.")

        case 4:
            display_tasks()

        case 5:
            print('Программа завершилась, всего доброго!')
            break

        case _:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")



