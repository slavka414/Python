# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

s1 = int(input('Введи первое число:   '))
s2 = int(input('Введи второе число:   '))
s3 = int(input('Введи третье число:   '))

def max_sum(sl1, sl2, sl3):
    l = [sl1, sl2, sl3]
    l.remove(min(sl1, sl2, sl3))
    return sum(l)

print(max_sum(s1, s2, s3))

