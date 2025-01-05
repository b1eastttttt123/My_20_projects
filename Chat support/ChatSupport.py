problem_list = []
answer_list = []


def login():
    print('Техническая поддержка - "Tokyo"\n')
    logins = input('Введите логин: ')
    passwords = input('Введите пароль: ')
    return logins, passwords


def check_credentials(log, passw):
    with open('credentials.txt', 'r') as file:
        credentials = file.readlines()
    return f"{log}:{passw}\n" in credentials


def admin_actions():
    print(f'\nДобро пожаловать, {login_user}!\n')
    while True:
        print('Открытые тикеты:')
        with open('problems_users.txt', 'r') as file:
            open_tickets = file.readlines()
        for ticket in open_tickets:
            print(ticket.strip())

        open_ticket = input('\nВведите название тикета: ')
        answer_ticket = input('Введите решение проблемы: ')
        answer_list.append(f"{open_ticket}: {answer_ticket}\n")

        with open('answer_support.txt', 'a') as file:
            file.write(f"{open_ticket}: {answer_ticket}\n")
            print(f'\nВы ответили на тикет: {open_ticket}\n')


def user_actions(logger):
    print(f'\nДобро пожаловать, {logger}!')
    while True:
        print('Выберите: ')
        print('1. Написать тикет')
        print('2. Посмотреть ответы')
        print('3. Выйти из учетной записи')

        function_selection = int(input('Напишите цифру: '))

        match function_selection:
            case 1:
                create_ticket()
            case 2:
                view_answers()
            case 3:
                print('Всего доброго')
                break


def create_ticket():
    print('\nСоздание тикета:')
    user_name = input('Введите имя: ')
    user_problem_name = input('Введите название тикета: ')
    user_problem = input('Введите описание проблемы: ')

    problem_list.append(f"{user_name}: {user_problem_name} - {user_problem}\n")

    with open('problems_users.txt', 'a') as file:
        file.writelines(problem_list)
        print(f'\nВаш тикет был сохранен под названием: {user_problem_name}\n')


def view_answers():
    print('\nПосмотреть ответы на Ваши тикеты:')
    with open('answer_support.txt', 'r') as file:
        answer_support = file.readlines()
    for answer in answer_support:
        print(answer.strip(), '\n')


# Основной поток программы
login_user, password_user = login()

if check_credentials(login_user, password_user):
    if login_user == "admin":
        admin_actions()
    else:
        user_actions(login_user)
else:
    print("\nНеверный логин или пароль.")
