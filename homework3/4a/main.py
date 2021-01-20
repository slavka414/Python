# Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

s1 = float(input('Введи первое число:   '))
s2 = int(input('Введи второе число:   '))
while s2 > 0:
    s2 = int(input('Введи второе число:   '))

def step (**kwargs):
#    return kwargs
    i = 1
    z = 1
    while i <= abs(kwargs.setdefault('y')):
        z = z * kwargs.setdefault('x')
        i += 1
    z = 1 / z
    return z

print(step(x=s1, y=s2))
