#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

debit = int(input('Введи дабит:  '))
credit = int(input('Введи кредит:  '))

result = debit - credit
print(f'Результат = {result}')
if result < 0:
    print('Ты в минусе')
elif result == 0:
    print('Ты на нуле')
elif result > 0:
    print('Ты в плюсе')
    serf = int(input('Введи количество рабочих:'))
    cash = result / serf
    print(f'Прибыль на одного человека = {cash} ')
    rentab = cash / result
    print(f'Рентабельность выручки = {rentab} ')
