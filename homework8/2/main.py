# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ODivision(Exception):
    def __init__(self, alarm):
        self.alarm = alarm

try:
    delim = int(input("Введи делимое:  "))
    delit = int(input("Введи делитель: "))
    if delit == 0:
        raise ODivision("Делить на 0 нельзя")
except (ValueError, ODivision) as err:
    print(err)
else:
    print(delim / delit)
