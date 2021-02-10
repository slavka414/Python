# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    surname = "Пупкин"
    def __init__(self, name, surname, wage, bonus, position):
        self._income = {"wage": wage, "bonus": bonus}
        self.p = position
        self.n = name
        self.s = surname

class Position(Worker):
    def get_full_name(self):
        print(f'{self.p}: {self.n} {self.s}')

    def get_total_income(self):
        inc = int(self._income.get("wage")) + int(self._income.get("bonus"))
        print(f'Оклад + Премия: {inc}')



work = Position("Вася", "Пупкин", 10000, 2000, "Врач")
work.get_full_name()
work.get_total_income()

