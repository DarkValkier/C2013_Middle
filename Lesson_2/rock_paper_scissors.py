import random

ITEMS = {
    'к': {
        'name': 'Камень',
        'win': ['н']
    },
    'н': {
        'name': 'Ножницы',
        'win': ['б']
    },
    'б': {
        'name': 'Бумага',
        'win': ['к']
    }
}

def choose_item(auto=False):
    if auto:
        return random.choice(list(ITEMS))

    while True:
        print(' к - Камень')
        print(' н - Ножницы')
        print(' б - Бумага')

        choice = input('\nВыберите предмет (к, н, б):').lower()

        if choice in ITEMS:
            return choice
        else:
            print('Попробуй ещё раз.')

def full_name(name):
    return ITEMS.get(name)['name']

def get_win_list(item):
    return ITEMS[item]['win']

def check_victory(player, enemy):
    '''

    Если предмет player`а побеждает предмет enemy, возвращается True
    Если предмет player`а проигрывает предмет enemy, возвращается False
    Если победителя установить не удалось, возвращается None

    '''
    # 'н' in get_win_list(player)
    if enemy in get_win_list(player):
        return True
    elif player in get_win_list(enemy):
        return False
    else:
        return None



print('--- ИГРА "КАМЕНЬ. НОЖНИЦЫ. БУМАГА" ---\n')

player_choice = choose_item()
bot_choice = choose_item(auto=True)

print(f'{full_name(player_choice)} vs {full_name(bot_choice)}')

if player_choice == bot_choice:
    print('Ничья!')
else:
    result = check_victory(player_choice, bot_choice)
    if result is None:
        print('Не удалось определить победителя.')
    elif result:
        print('Победа игрока')
    else:
        print('Победа компьютера')
