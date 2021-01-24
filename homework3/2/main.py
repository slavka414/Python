# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

n = str(input('Введите имя:   '))
s = str(input('Введите фамилию:   '))
yb = int(input('Введите год рождения:   '))
t = str(input('Введите город проживания:   '))
e = str(input('Введите e-mail:   '))
p = int(input('Введите телефон:   '))

def new_user (name, surname, year_born, town,email, phone):
    print(f'{name} {surname} {year_born} {town} {email} {phone}')

new_user(name=n, surname=s, year_born=yb, town=t, email=e, phone=p)


