var_1 = int(input("Введите количество рядов: "))
for i in range(var_1, 0, -1):
    print((var_1-i) * ' ' + i * '*')
