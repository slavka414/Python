#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
num = int(input('Введи число:  '))
while True:
    a = num % 10
    b = (num // 10) % 10
    if b > a:
        c = b
    if (num < 10):
        print(f'Число {c} самое большое')
        break
    else:
        num = num // 10
        continue