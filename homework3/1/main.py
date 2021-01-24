#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

del1 = int(input('Введи делимое:   '))
del2 = int(input('Введи делитель:   '))

def del_en (delim, delit):
    return delim / delit

try:
    del2 == 0
    print(del_en(del1, del2))
except ZeroDivisionError:
    print('На ноль делить нельзя!')
    pass