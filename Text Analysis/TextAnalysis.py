def find_words():
    with open('text.txt', 'r') as file:
        words = file.read().split()
    print(f'\nTotal words: {len(words)}\n')


def find_symbol():
    with open('text.txt', 'r') as file:
        symbol = file.read()
        all_symbol = set('`!@#$%^&*()!"№%:,.;()_~?}{[]')
        num_symbols = sum(symbol.count(s) for s in all_symbol)
    print(f'\nTotal number of symbols: {num_symbols}\n')


def find_spaces():
    with open('text.txt', 'r') as file:
        space = file.read()
        print(f'\nSpaces: {space.count(" ")}\n')


print('Welcome to system: "Text analysis"')
print('\nYou need to paste into the "text.txt" - your text!\n')

while True:
    try:
        print('Choose what we will look for: ')
        print('1. Find words')
        print('2. Find symbol')
        print('3. Find spaces')
        choose = int(input('Write here -> '))

        match choose:
            case 1:
                find_words()
            case 2:
                find_symbol()
            case 3:
                find_spaces()
            case _:
                print('\nError: there is no such number!\n')

    except ValueError:
        print('\nERROR: enter a number!\n')


