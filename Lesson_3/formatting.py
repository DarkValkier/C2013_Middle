# Форматирование строк

a = 'Hello world!'
width = 50
align = '^'
symbol = '='


# print(f'{" " + a + " ":=^30}')
print(f'{f" {a} ":{symbol}{align}{width}}')

# ===== Hello world! =====