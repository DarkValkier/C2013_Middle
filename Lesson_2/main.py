import random


def generate_number(a, b):
    return random.randint(a, b)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(f'Случайное число в диапазоне от {a} до {b} - {generate_number(a, b)}')