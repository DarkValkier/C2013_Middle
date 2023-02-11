# Таблица умножения
from colorama import Fore, Back, Style

for i in range(20):
    for j in range(20):
        if i == 0 and j == 0:
            print(f'{Fore.LIGHTWHITE_EX}{Back.YELLOW}{"":^5}', end='')
        elif i == 0:
            print(f"{Fore.LIGHTWHITE_EX}{Back.YELLOW}{j:^5}", end='')
        elif j == 0:
            print(f"{Fore.LIGHTWHITE_EX}{Back.YELLOW}{i:^5}", end='')
        else:
            print(f'{Fore.BLACK}{Back.LIGHTWHITE_EX}{i*j:^5}', end='')
        print(Style.RESET_ALL, end='')
    print()