# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
path, work_time, time_cost, bonus = argv
print(argv)
try:
    work_time = int(work_time)
    time_cost = int(time_cost)
    bonus = int(bonus)
    money = (work_time * time_cost) + bonus
    print(f'Зарплата составляет:   {money}')

except ValueError:
    print('Введены неправильные данные')



