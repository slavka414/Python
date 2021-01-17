#utf8
#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input('Просто введи одну цифру   '))

ten_num = (num * 10) + num
hundred_num = (num * 100) + ten_num

print(f'А вот что получилось {num} + {ten_num} + {hundred_num} = {num + ten_num + hundred_num}')
